from googleapiclient.discovery import build
import base64
import google.auth
import os

def hello_pubsub():   
 
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bkt-dataflow-metadata/udf.js",
        "JSONPath": "gs://bkt-dataflow-metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "prj-poc-001:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://bkt-dataflow-metadata/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-dataflow-metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

hello_pubsub()





from googleapiclient.discovery import build


def trigger_df_job(cloud_event):   
 
    service = build('dataflow', 'v1b3')
    project = "tt-sandbox-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "p-prac",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://sid_bucket_01/udf.js",
        "JSONPath": "gs://sid_bucket_01/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "tt-sandbox-001.siddhesh.salunke",
        "inputFilePattern": "gs://dl-agent/batsmen_rankings2.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://sid_bucket_01",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

