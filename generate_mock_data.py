import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import boto3
import os

def generate_sentiment_data():
    stocks = ['AAPL', 'TSLA', 'MSFT', 'AMZN']
    start_date = datetime(2025, 4, 1)
    data = []

    for stock in stocks:
        for i in range(25):  # 25 rows per stock = 100 total
            date = start_date + timedelta(days=i)
            sentiment_score = np.random.uniform(-1, 1)
            source_text = f"Mock sentiment for {stock} on {date.strftime('%Y-%m-%d')}"
            data.append({
                'symbol': stock,
                'date': date.strftime('%Y-%m-%d'),
                'sentiment_score': round(sentiment_score, 2),
                'source_text': source_text
            })

    return pd.DataFrame(data)

def save_and_upload_csv(df, bucket_name, s3_key):
    local_file = 'stocks_sentiment.csv'
    df.to_csv(local_file, index=False)
    print(f"Saved {local_file} locally")

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    df = generate_sentiment_data()
    print(f"Generated {len(df)} rows of sentiment data")
    bucket_name = 'market-analysis-tool'  # Adjust if using market-analysis-tool
    s3_key = 'sentiment/stocks_sentiment.csv'
    save_and_upload_csv(df, bucket_name, s3_key)
