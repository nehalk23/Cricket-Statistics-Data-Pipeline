


![image](https://github.com/user-attachments/assets/cb4dbdea-1da2-4135-b305-6e99b12e43dc)



# Cricbuzz Data Pipeline with Google Cloud

This project demonstrates an end-to-end data pipeline that extracts cricket statistics using Python and the Cricbuzz API, stores the data in Google Cloud Storage, processes it with Dataflow, and visualizes it using Looker Studio.

---

## Project Flow Overview

### 1. Data Retrieval with Python & Cricbuzz API
We begin by leveraging Python to interface with the Cricbuzz API, allowing us to fetch real-time cricket statistics and match data. Python’s robust HTTP and JSON libraries make this integration seamless and efficient.

---

### 2. Storing Data in Google Cloud Storage (GCS)
Fetched data is transformed into CSV format and uploaded to a Google Cloud Storage (GCS) bucket. This ensures durable, scalable, and accessible storage, ready for further processing.

---

### 3. Creating a Cloud Function Trigger
A Google Cloud Function is set up to trigger automatically upon file upload to GCS. This serverless function initiates the processing pipeline whenever new data is ingested.

---

### 4. Execution of the Cloud Function
The Cloud Function contains logic to launch a Dataflow job. It passes the required parameters like input file location, BigQuery table destination, and temporary storage paths, ensuring automated orchestration.

---

### 5. Dataflow Job for BigQuery
The heart of the pipeline lies in the Dataflow job. Triggered by the Cloud Function, it transfers the CSV data from GCS to BigQuery. The job is configured for performance and reliability to ensure clean, efficient data ingestion.

---

### 6. Looker Dashboard Creation
Finally, BigQuery serves as the data source for Looker Studio. We configure a Looker dashboard that connects to BigQuery and presents the ingested cricket data in a visually rich and interactive format for insights and analysis.

![image](https://github.com/user-attachments/assets/afcdbfc7-768c-41a7-ae7b-288b7c2527d6)

---

## Technologies Used

- Python
- Cricbuzz API
- Google Cloud Storage (GCS)
- Google Cloud Functions
- Google Dataflow
- Google BigQuery
- Looker Studio

---

## Folder Structure (optional)

