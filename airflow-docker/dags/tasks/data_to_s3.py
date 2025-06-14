import pandas as pd
import gspread
import boto3
import awswrangler as wr 
from airflow.models import Variable
from datetime import datetime



client = gspread.service_account(filename="credentials.json")  
spreadsheet = client.open("spread.com")

worksheet = spreadsheet.sheet1

# Get all data from the worksheet
rows = worksheet.get_all_values()
def records():

    mates_record = pd.DataFrame(rows[1:], columns=rows[0])
    cleaned_columns = []
    for col in mates_record.columns:
        col = col.strip().strip('"')
        col = ' '.join(col.split())
        col = col.lower()
        col = col.replace(" ", "_")
        cleaned_columns.append(col)
    mates_record.columns = cleaned_columns
        
    session = boto3.Session(
            aws_access_key_id=Variable.get('ACCESS_KEY'),
            aws_secret_access_key=Variable.get('SECRET_KEY'),
            region_name='eu-central-1'
    )
    date_str = datetime.today().strftime('%Y-%m-%d')
    path=f's3://kaycee-gs-data/mentees_data/google_sheet_{date_str}.parquet'

    wr.s3.to_parquet(
            df=mates_record,
            path= path,
            dataset=False,
            boto3_session=session
    )
    return mates_record
        
