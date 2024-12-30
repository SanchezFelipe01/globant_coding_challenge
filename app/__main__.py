import os
from flask import Flask, render_template
from config.db_config import Config
from models.models import db, Department, Job, Employee
from logic import departments_crud, jobs_crud, employees_crud


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_departments_path = os.path.join(current_directory, '..', 'files', 'departments.csv')

@app.route('/')
def home():
    return render_template('main_page.html')

### DEPARTMENTS ###

@app.route('/import_departments_csv')
def import_departments_csv():
   return departments_crud.import_departments_csv(db, Department, csv_departments_path)


@app.route('/get_all_departments')
def get_all_departments():
    return departments_crud.get_all_departments(Department)


@app.route('/delete_all_departments')
def delete_all_departments():
    return departments_crud.delete_all_departments(db, Department)

### DEPARTMENTS ###

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)