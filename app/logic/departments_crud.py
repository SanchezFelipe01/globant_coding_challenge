import os, sys
sys.path.append(os.path.dirname(__file__))

from helpers import import_csv, get_all_records, delete_all_records


def import_departments_csv(db, department, csv_departments_path: str):
    return import_csv(db, department, csv_departments_path, ['id', 'department'])

def get_all_departments(department):
    return get_all_records(department, 'departments.html')

def delete_all_departments(db, department):
    return delete_all_records(db, department)