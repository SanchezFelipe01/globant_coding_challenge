import os
from flask import Flask, render_template
from config.db_config import Config
from models.models import db, Department, Job, Employee
from logic import departments_crud, jobs_crud, employees_crud, custom_queries


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_departments_path = os.path.join(current_directory, '..', 'files', 'departments.csv')
csv_jobs_path  = os.path.join(current_directory, '..', 'files', 'jobs.csv')
csv_employees_path = os.path.join(current_directory, '..', 'files', 'hired_employees.csv')

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

### JOBS ###

@app.route('/import_jobs_csv')
def import_jobs_csv():
    return jobs_crud.import_jobs_csv(db, Job, csv_jobs_path)


@app.route('/get_all_jobs')
def get_all_jobs():
    return jobs_crud.get_all_jobs(Job)
    
@app.route('/delete_all_jobs')
def delete_all_jobs():
    return jobs_crud.delete_all_jobs(db, Job)

### JOBS ###

### EMPLOYEES ###

@app.route('/import_employees_csv')
def import_employees_csv():
    return employees_crud.import_employees_csv(db, Employee, csv_employees_path)

@app.route('/get_all_employees')
def get_all_employees():
    return employees_crud.get_all_employees(Employee)

@app.route('/get_employees_missing_info')
def get_employees_with_missing_info():
    return employees_crud.get_employees_with_missing_info(Employee)

@app.route('/delete_all_employees')
def delete_all_employees():
    return employees_crud.delete_all_employees(db, Employee)

### EMPLOYEES ###

### QUERIES ###

@app.route('/recruitments')
def get_quarterly_recruitments():
    return custom_queries.recruitments_by_quarter(db, Department, Job, Employee)

@app.route('/people_by_departments')
def get_people_by_departments():
    return custom_queries.people_by_department(db, Department, Employee)

### QUERIES ###

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)