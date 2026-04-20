# 📊 Data Pipeline for Processing CSV Files on AWS

![Project Banner]()

## 🚀 Project Overview

This project demonstrates how to build a scalable, event-driven data pipeline on AWS.

CSV files are uploaded to an S3 raw bucket
An AWS Lambda function is triggered automatically
Data is cleaned and stored in a processed S3 bucket
AWS Glue performs ETL operations
Final data is stored in a final S3 bucket
Amazon QuickSight is used for data visualization

---
## 🏗️ Architecture Overview

🔹 High-Level Workflow
Upload CSV file to csv-raw-data bucket
S3 event triggers AWS Lambda
Lambda preprocesses and stores data in csv-processed-data
AWS Glue Crawler scans and creates schema
AWS Glue Job transforms data
Output stored in csv-final-data
Amazon QuickSight visualizes data

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
## 2️⃣ Configure AWS Lambda
``` bash
● Runtime: Python 3.x
● Trigger: S3 (on object upload)
● Functionality:
   ● Read CSV file
   ● Clean/transform data
   ● Save to processed bucket
```
## 3️⃣ Setup AWS Glue
``` bash
✔️ Crawler
   ● Source: csv-processed-data
   ● Output: Glue Data Catalog
✔️ ETL Job
    ● Input: Catalog table
    ● Transform data
    ● Output: csv-final-data
``` 
## 4️⃣ Configure Amazon QuickSight
``` bash
● Connect to Glue Data Catalog / S3
● Create dataset
● Build dashboard
``` 
---

## 📊 AWS Console Snapshots 


## 🗂️ S3 Buckets
![VPC Dashboard](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/vpc-dashboard.png)

---

## 📊 ALB Overview Page
![ALB Overview](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/alb-overview.png)

---

## 📊 Target Group – Healthy Targets

![TG](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/target-group-healthy-instances.png)

---
## 📊 Auto Scaling Group – Activity History


![Auto Scaling Group – Activity](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/asg-scaling-activity-history.png)

---

## 📊 CloudWatch CPU Utilization Graph
![CloudWatch CPU Utilization Graph](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/cpu-utlization-graph-cw.png)

---

## 📊 CloudWatch Target tracking RequestCountPerTarget Graph 

![CloudWatch Target tracking RequestCountPerTarget Graph](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/Target-tracking-scaling-cloudwatch-alarm-graph.png)

## 📊 CloudWatch UnHealthyHostCount Alarm
![CloudWatch UnHealthyHostCount Graph](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/unhealthy-host-count-cloudwatch-graph.png)

---
![CloudWatch UnHealthyHostCount Alert](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/unhealthy-hostcount-alert-via-cloudwatch-alarm.png)

---

## 📊 Scaling Policy (RequestCountPerTarget)
![Scaling Policy - (RequestCountPerTarget)](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/asg-target-tracking-policy.png)

---

## 📊 EC2 Instances List (Multiple Instances Running)
![ EC2 Instances](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/ec2-instances-multiples.png)

---

## 🌐 Application Preview (Deployed)
![ Netflix Web app](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/application-view-1.png)

---
![ Netflix Web app-features](https://github.com/biswarup65/Netflix-WebApp-Aws/blob/main/screenshots/application-view-2.png)

---

## 🧪 Testing & Validation

● Verified traffic distribution across EC2 instances

● Simulated instance failure and observed auto-healing

● Generated load to trigger auto scaling

● Confirmed CloudWatch alarms and scaling behavior

---

## 📈 Learning Outcomes

➤ Hands-on experience with highly available cloud architecture

➤ Practical understanding of monitoring and alerting

➤ Learned real-world troubleshooting scenarios

➤ Gained exposure to AWS best practices for operations


---

## 🏁 Conclusion

This project demonstrates a production-style AWS infrastructure focused on availability, scalability, monitoring, and security.
It reflects real-world cloud support responsibilities and provides a strong foundation in Cloud Infrastructure.

---
## References

- AWS Documentation: VPC with servers in private subnets and NAT gateway  
  https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html

- AWS Documentation: VPC for Web and Database servers 
  https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-web-database-servers.html



