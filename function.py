from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "tt-sandbox-001"

    template_path = "gs://dataflow-templates-us-west1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://dl-agent/udf.js",
        "JSONPath": "gs://dl-agent/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "tt-sandbox-001.siddhesh.etl-prac-",
        "inputFilePattern": "gs://dl-agent/batsmen_rankings2.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dl-agent/temp",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

