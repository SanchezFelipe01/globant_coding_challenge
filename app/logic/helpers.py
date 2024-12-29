import pandas as pd
from sqlalchemy import inspect
import csv
from flask import render_template, jsonify

### AUX FUNCTIONS ###

def record_exists_by_id(session, model, record_id):
    table_model = session.get(model, record_id)
    return table_model is not None

def import_csv(db, model, csv_path: str, columns: list):
    message = ""
    try:
        inspector = inspect(db.engine)
        if not inspector.has_table(model.__table__.name):
            db.create_all()

        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

            for row in data:
                record_data = {columns[i]: (int(row[i]) if row[i].isdigit() else row[i]) for i in range(len(columns))}
                if not record_exists_by_id(db.session, model, record_data['id']):
                    record = model(**record_data)
                    db.session.add(record)
            db.session.commit()
        message = "Records successfully imported."
    except Exception as e:
        db.session.rollback()
        message = f"Error while importing the records: {str(e)}"
    return jsonify({"message": message})


def get_all_records(model, template_name: str, title: str = None):
    try:
        records = model.query.all()
        return render_template(template_name, records=records, title=title)
    except Exception:
        return render_template(template_name, title=title)
    

def delete_all_records(db, model):
    message = ""
    try:
        db.session.query(model).delete()
        db.session.commit()
        message = "All records from the table have been deleted."
    except Exception as e:
        db.session.rollback()
        message = f"Error while deleting the records: {str(e)}"
    return jsonify({"message": message})

### AUX FUNCTIONS ###