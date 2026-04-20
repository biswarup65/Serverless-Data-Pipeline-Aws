# 📊 Data Pipeline for Processing CSV Files on AWS

![Project Banner]()

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

## Raw bucket (csv-raw-data)
![Raw bucket]()

## Raw bucket (csv-raw-data)
![Raw bucket]()

## Processed bucket (csv-processed-data)
![Processed]()

---

## ⚡Lambda

## Lambda function configuration
![Lambda function configuration]()

## Execution logs (CloudWatch)
![Execution logs]()

---

## 🔄 AWS Glue

## Glue Crawler configuration
![Glue Crawler configuration]()

## Glue Data Catalog tables
![Glue Data Catalog tables]()

## Glue ETL Job run details
![Glue ETL Job run details]()
---

## 📊 QuickSight

## Dashboard visualization
![Dashboard visualization]()

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

## 🏁 Conclusion

This project demonstrates a production-style AWS infrastructure focused on availability, scalability, monitoring, and security.
It reflects real-world cloud support responsibilities and provides a strong foundation in Cloud Infrastructure.

---




