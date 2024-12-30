import os, sys
sys.path.append(os.path.dirname(__file__))

from helpers import import_csv, get_all_records, delete_all_records


def import_jobs_csv(db, job, csv_jobs_path: str):
    return import_csv(db, job, csv_jobs_path, ['id', 'job'])

def get_all_jobs(job):
    return get_all_records(job, 'jobs.html')

def delete_all_jobs(db, job):
    return delete_all_records(db, job)
