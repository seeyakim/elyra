from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "badbad-0616094801",
}

dag = DAG(
    "badbad-0616094801",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using badbad.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_2e2313d2_b183_47fb_86a5_fc1379102aa8 = NotebookOp(
    name="badboy",
    namespace="admin",
    task_id="badboy",
    notebook="Desktop/test/elyra_flatform/badboy.py",
    cos_endpoint="http://localhost:9000/",
    cos_bucket="airflow-pipeline-artifacts",
    cos_directory="badbad-0616094801",
    cos_dependencies_archive="badboy-2e2313d2-b183-47fb-86a5-fc1379102aa8.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="continuumio/anaconda3:2020.07",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)
