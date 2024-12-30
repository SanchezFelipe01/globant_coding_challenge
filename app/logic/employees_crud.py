import os, sys
sys.path.append(os.path.dirname(__file__))

from helpers import import_csv, get_all_records, delete_all_records
from flask import render_template, jsonify
from sqlalchemy.sql import or_


def import_employees_csv(db, employee, csv_employees_path: str):
    return import_csv(db, 
                      employee, 
                      csv_employees_path, 
                      ['id', 'name', 'datetime', 'department_id', 'job_id'])

def get_all_employees(employee):
    return get_all_records(employee, 'employees.html', title='Hired employees')

def delete_all_employees(db, employee):
    return delete_all_records(db, employee)

def get_employees_with_missing_info(employee):
    try:
        employees = employee.query.filter(
            or_(
                employee.name.is_(None),
                employee.datetime.is_(None),
                employee.department_id.is_(None),
                employee.job_id.is_(None),
            )
        ).all()
        return render_template('employees.html', 
                               records=employees, 
                               title='Employees with missing information')
    except Exception:
        return render_template('employees.html', 
                               title='Employees with missing information')
