# 📊 Data Pipeline for Processing CSV Files on AWS

![Project Banner](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/serverless-csv-data-pipeline-architectural-diagram.png)

## 🚀 Project Overview

This project demonstrates how to build a scalable, event-driven data pipeline on AWS.

● CSV files are uploaded to an S3 raw bucket 

● An AWS Lambda function is triggered automatically 

● Data is cleaned and stored in a processed S3 bucket 

● AWS Glue performs ETL operations 

● Final data is stored in a final S3 bucket 

● Amazon QuickSight is used for data visualization 

---
## 🏗️ Architecture Overview

🔹 High-Level Workflow: 

1️⃣ Upload CSV file to csv-raw-data bucket

2️⃣ S3 event triggers AWS Lambda

3️⃣ Lambda preprocesses and stores data in csv-processed-data

4️⃣ AWS Glue Crawler scans and creates schema

5️⃣ AWS Glue Job transforms data

6️⃣ Output stored in csv-final-data

7️⃣ Amazon QuickSight visualizes data

---


## 🧰 Services Used

| AWS Services | Purpose |
|-----------|-------|
| **Amazon S3** | Storage for raw, processed, and final data |
| **AWS Lambda** | Serverless compute for preprocessing CSV files |
| **AWS Glue** | ETL (Extract, Transform, Load) operations |
| **Amazon QuickSight** | Data visualization and dashboards |
| **IAM Roles & Policies** | Secure access control between services |


---

## ⚙️ Setup Instructions

## 1️⃣ Create S3 Buckets
``` bash
 ● csv-raw-data
 ● csv-processed-data
 ● csv-final-data
```
## 2️⃣ IAM Permissions 
``` bash
Ensure proper IAM roles:
 • Lambda → S3 access
 • Glue → S3 + Catalog access
 • QuickSight → S3/Glue access
```

## 3️⃣ Configure AWS Lambda
``` bash
● Runtime: Python 3.x
● Trigger: S3 (on object upload)
● Functionality:
   ● Read CSV file
   ● Clean/transform data
   ● Save to processed bucket
```
## 4️⃣ Setup AWS Glue
``` bash
✔️ Crawler
   ● Source: csv-processed-data
   ● Output: Glue Data Catalog
✔️ ETL Job
    ● Input: Catalog table
    ● Transform data
    ● Output: csv-final-data
``` 
## 5️⃣ Configure Amazon QuickSight
``` bash
 ● Connect to Glue Data Catalog / S3
 ● Create dataset
 ● Build dashboard
``` 
---

## 📊 AWS Console Snapshots 


## 🗂️ S3 Buckets

## ● Raw bucket (csv-raw-data)
![Raw bucket](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20173505.png)

## ● Processed bucket (csv-processed-data)
![Processed bucket](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20173531.png)

## ● Final bucket (csv-final-data)
![Final bucket](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20173556.png)

---

## ⚡Lambda

## ● Lambda function configuration
![Lambda function configuration](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20173812.png)



---

## 🔄 AWS Glue

## ● Glue Crawler configuration
![Glue Crawler configuration](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20174520.png)

## ● Glue Data Catalog tables
![Glue Data Catalog tables](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20174623.png)

## ● Glue ETL Job run details
![Glue ETL Job run details](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20175059.png)

![Glue ETL Job run details](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20175820.png)
---

## 📊 QuickSight

## ● Dashboard visualization
![Dashboard visualization-1](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20190453.png)

![Dashboard visualization-2](https://github.com/biswarup65/Serverless-Data-Pipeline-Aws/blob/main/screenshots/Screenshot%202026-04-20%20190541.png)



---


## 🧠 Key Features
✅ Fully serverless architecture

✅ Event-driven processing

✅ Scalable and cost-efficient

✅ Automated ETL pipeline

✅ Real-time data visualization

---

## 🎯 Learning Outcomes
● Hands-on with AWS core services (S3, Lambda, Glue)

● Understanding of ETL pipelines

● Experience with event-driven architecture

● Data visualization using QuickSight

● IAM roles and permissions management



---

## 📌 Conclusion

This project demonstrates how to build a fully serverless, scalable, and event-driven data pipeline on AWS using S3, Lambda, AWS Glue, and QuickSight. It highlights the practical implementation of data ingestion, transformation, and visualization in a real-world scenario.

By completing this project, you gain hands-on experience with core AWS services, understand ETL workflows, and learn how to design efficient cloud-based data solutions.

---




