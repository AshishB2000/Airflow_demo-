from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta


default_args={
    'owner' : 'Ashish',
    'start_date' : datetime(2024,5,24)
}




dag= DAG(

    dag_id= 'etl1',
    default_args= default_args,
    schedule_interval= None,
    catchup=False,
    tags=['etl1','etl_demo']
)

start=DummyOperator(task_id= "start",dag=dag)
extract= DummyOperator(task_id= "ectract",dag=dag)
transform= DummyOperator(task_id= "transform",dag=dag)
load= DummyOperator(task_id= "load",dag=dag)
end= DummyOperator(task_id= "end",dag=dag)

start>> extract  >> transform >> load >> end