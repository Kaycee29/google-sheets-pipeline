# 📊 Spreadsheet  Pipeline - Automating  Google Sheets Data to AWS DataLake

This project automates the process of extracting data from a Google Sheet and uploading it directly into a data lake (AWS S3) using a stack of modern data tools like Apache Airflow, Docker, and Terraform.

✅ What Does it Do?

   1ststep: it Connects to a Google Sheet to extract structured data

   2ndstep: Uses Airflow to schedule and automate the pipeline

   3rd step:  Runs inside Docker containers for portability and consistency

   4th step : Terraform provisions the S3 bucket (data lake)

  final step: Uploads the data to AWS S3 for long-term storage or analysis

🧰 Tools Used

   Airflow – for orchestration and scheduling

   Docker – to containerize the whole pipeline

   Terraform – to set up cloud infrastructure (S3 bucket)

   AWS S3 – as a cloud data lake

   Python – for Google Sheets API and S3 integration

💡 Why I Built This

To gain hands-on experience with building real-world data pipelines that move data from spreadsheets into a cloud storage system — automatically, reliably, and on a schedule.

This setup is perfect for recurring reports and  dashboards
