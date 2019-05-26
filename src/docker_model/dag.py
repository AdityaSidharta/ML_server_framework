from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'adi',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email': ['hello@adityasidharta.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval': '*/5 * * * *'
}


dag = DAG('airflow_model', catchup=False, default_args=default_args)
