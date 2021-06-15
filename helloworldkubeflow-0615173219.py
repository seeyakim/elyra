from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "helloworldkubeflow-0615173219",
}

dag = DAG(
    "helloworldkubeflow-0615173219",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using helloworldkubeflow.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_05e5edd3_9ad4_4f7e_a0c7_183197bb9e97 = NotebookOp(
    name="loaddata",
    namespace="admin",
    task_id="loaddata",
    notebook="Desktop/test/hello/loaddata.ipynb",
    cos_endpoint="http://localhost:9000/",
    cos_bucket="airflow-pipeline-artifacts",
    cos_directory="helloworldkubeflow-0615173219",
    cos_dependencies_archive="loaddata-05e5edd3-9ad4-4f7e-a0c7-183197bb9e97.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
    },
    config_file="None",
    dag=dag,
)


notebook_op_5eac24a7_7a1d_4542_91fd_065f1bed4005 = NotebookOp(
    name="DataCleaning",
    namespace="admin",
    task_id="DataCleaning",
    notebook="Desktop/test/hello/DataCleaning.ipynb",
    cos_endpoint="http://localhost:9000/",
    cos_bucket="airflow-pipeline-artifacts",
    cos_directory="helloworldkubeflow-0615173219",
    cos_dependencies_archive="DataCleaning-5eac24a7-7a1d-4542-91fd-065f1bed4005.tar.gz",
    pipeline_outputs=["data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv"],
    pipeline_inputs=["data/noaa-weather-data-jfk-airport/jfk_weather.csv"],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5eac24a7_7a1d_4542_91fd_065f1bed4005 << notebook_op_05e5edd3_9ad4_4f7e_a0c7_183197bb9e97


notebook_op_9931311a_f423_473e_b474_8fe66f11d9e8 = NotebookOp(
    name="Part_2___Data_Analysis",
    namespace="admin",
    task_id="Part_2___Data_Analysis",
    notebook="Desktop/test/hello/Part 2 - Data Analysis.ipynb",
    cos_endpoint="http://localhost:9000/",
    cos_bucket="airflow-pipeline-artifacts",
    cos_directory="helloworldkubeflow-0615173219",
    cos_dependencies_archive="Part 2 - Data Analysis-9931311a-f423-473e-b474-8fe66f11d9e8.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv",
        "data/noaa-weather-data-jfk-airport/jfk_weather.csv",
    ],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9931311a_f423_473e_b474_8fe66f11d9e8 << notebook_op_5eac24a7_7a1d_4542_91fd_065f1bed4005


notebook_op_b70a0fb1_4a34_4fbb_a9a4_3a11bfcf8f00 = NotebookOp(
    name="Part_3___Time_Series_Forecasting",
    namespace="admin",
    task_id="Part_3___Time_Series_Forecasting",
    notebook="Desktop/test/hello/Part 3 - Time Series Forecasting.ipynb",
    cos_endpoint="http://localhost:9000/",
    cos_bucket="airflow-pipeline-artifacts",
    cos_directory="helloworldkubeflow-0615173219",
    cos_dependencies_archive="Part 3 - Time Series Forecasting-b70a0fb1-4a34-4fbb-a9a4-3a11bfcf8f00.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv",
        "data/noaa-weather-data-jfk-airport/jfk_weather.csv",
    ],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_b70a0fb1_4a34_4fbb_a9a4_3a11bfcf8f00 << notebook_op_5eac24a7_7a1d_4542_91fd_065f1bed4005
