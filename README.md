<<<<<<< HEAD
# Building a Cricket Statistics Pipeline with Google Cloud Services

In the world of data engineering, the journey from data retrieval to insightful visualization is an adventure filled with challenges and rewards. In this guide, we’ll walk through the intricate steps of constructing a comprehensive cricket statistics pipeline using Google Cloud services. From retrieving data via the Cricbuzz API to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.

### Architecture

![Architecture](https://github.com/vishal-bulbule/cricket-stat-data-engineering-project/blob/master/Architecture.png)

### Data Retrieval with Python and Cricbuzz API
The foundation of our project begins with Python’s prowess in interfacing with APIs. We’ll delve into the methods of fetching cricket statistics from the Cricbuzz API, harnessing the power of Python to gather the required data efficiently.

### Storing Data in Google Cloud Storage (GCS)
Once the data is obtained, our next step involves preserving it securely in the cloud. We’ll explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.

### Creating a Cloud Function Trigger
With our data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for our pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps.

### Execution of the Cloud Function
Within the Cloud Function, intricate code is crafted to precisely trigger a Dataflow job. We’ll meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing.

### Dataflow Job for BigQuery
The core of our pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. We’ll meticulously configure the job settings to ensure optimal performance and accurate data ingestion into BigQuery.

### Looker Dashboard Creation
Finally, we’ll explore the potential of BigQuery as a data source for Looker Studio. Configuring Looker to connect with BigQuery, we’ll create a visually compelling dashboard. This dashboard will serve as the visualization hub, enabling insightful analysis based on the data loaded from our cricket statistics pipeline.
![Looker](https://github.com/vishal-bulbule/cricket-stat-data-engineering-project/blob/master/Looker.png)
=======



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
- Looker 

---


>>>>>>> 5a49a577e8ade99479ffc061c25e3ba0dd545220
