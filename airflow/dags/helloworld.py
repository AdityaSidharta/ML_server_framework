from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'aditya',
    'depends_on_past': False,
    'start_date': datetime(2016, 8, 12),
    'email': ['aditya.sdrt@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Helloworld', default_args=default_args)

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(
    task_id='start',
    bash_command='echo "Start Operation"',
    dag=dag)

cmd = "./libs/run_docker_model.sh "
t2 = BashOperator(
    task_id='code',
    bash_command=cmd,
    dag=dag)

t3 = BashOperator(
    task_id='end',
    bash_command='echo "End"',
    dag=dag)

t1 >> t2 >> t3