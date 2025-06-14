from airflow import DAG
from airflow.operators.python import PythonOperator
from tasks.data_to_s3 import records
from datetime import datetime

default_args = {
    'owner': 'kaycee',
    'retries': 1
}

dag = DAG(
    dag_id = "daily_gsheet_data_to_s3",
    description = "This is my dag for daily weather extraction to s3",
    start_date = datetime(2025,6,12),
    schedule_interval = "0 12 * * *", # runs daily at 12pm
    catchup= False,
    default_args = default_args
    )

extract_to_s3 = PythonOperator(
    task_id = "extract_to_s3",
    dag = dag,
    python_callable = records
    )

extract_to_s3
