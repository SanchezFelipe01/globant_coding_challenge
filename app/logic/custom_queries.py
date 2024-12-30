import pandas as pd
from flask import render_template, jsonify

def recruitments_by_quarter(db, Department, Job, Employee):

    columns = ['department', 'job', 'Q1', 'Q2', 'Q3', 'Q4']
    df = pd.DataFrame(columns=columns)

    try:
        departments = pd.read_sql_table(Department.__tablename__, db.engine)
        jobs = pd.read_sql_table(Job.__tablename__, db.engine)
        hired_employees = pd.read_sql_table(Employee.__tablename__, db.engine)

        if hired_employees.empty or departments.empty or jobs.empty:
            return render_template('result.html', result=df, title='Recruitments per quarter')

        hired_employees['datetime'] = pd.to_datetime(hired_employees['datetime'])
        hired_employees_2021 = hired_employees[hired_employees['datetime'].dt.year == 2021].copy()

        hired_employees_2021['quarter'] = hired_employees_2021['datetime'].dt.quarter

        merged_df = pd.merge(
            hired_employees_2021, 
            departments, 
            left_on='department_id', 
            right_on='id'
        )
        
        merged_df = pd.merge(
            merged_df, 
            jobs, 
            left_on='job_id', 
            right_on='id'
        )
        
        result_df = (
            merged_df.groupby(['department', 'job', 'quarter'])
                .size().unstack(fill_value=0).reset_index()
        )

        result_df.columns = ['department', 'job', 'Q1', 'Q2', 'Q3', 'Q4']

        result_df = (
            result_df.sort_values(by=['department', 'job'])
                .reset_index(drop=True)
        )

        result_df.index = result_df.index +1
        return render_template('result.html', result=result_df, title='Recruitments per quarter')
    except Exception:
        df.loc[0] = 'Error'
        return render_template('result.html', result=df, title='Recruitments per quarter')

# REQUIREMENT 1

# REQUIREMENT 2

def people_by_department(db, Department, Employee):

    columns = ['id', 'department', 'hired']
    df = pd.DataFrame(columns=columns)

    try:

        departments = pd.read_sql_table(Department.__tablename__, db.engine)
        hired_employees = pd.read_sql_table(Employee.__tablename__, db.engine)

        if hired_employees.empty or departments.empty:
            columns = ['id', 'department', 'hired']
            df = pd.DataFrame(columns=columns)
            return render_template('result.html', result=df, title='People by department')

        hired_employees['datetime'] = pd.to_datetime(hired_employees['datetime'])
        hired_employees_2021 = hired_employees[hired_employees['datetime'].dt.year == 2021]

        merged_df = pd.merge(
            hired_employees_2021, 
            departments, 
            left_on='department_id', 
            right_on='id')

        merge2 = (
            merged_df.groupby(['id_y', 'department'])
                .size().reset_index(name='hired')
        )
        
        avg_num_employees_hired = merge2['hired'].mean()

        people_by_department_df = merge2[merge2['hired'] > avg_num_employees_hired]

        people_by_department_df = (
            people_by_department_df.sort_values(by='hired', ascending=False)
                .reset_index(drop=True)
        )

        people_by_department_df.rename(columns={'id_y': 'id'}, inplace=True)
        people_by_department_df.index = people_by_department_df.index +1
        return render_template('result.html', result=people_by_department_df, title='People by department')

    except Exception:
        df.loc[0] = 'Error'
        return render_template('result.html', result=df, title='People by department')

# REQUIREMENT 2