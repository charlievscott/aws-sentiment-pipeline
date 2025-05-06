# Multi-Modal Sentiment Analysis and Work Order Pipeline

## Overview
An AI system for analyzing feedback and stock sentiment, integrating text and image data with AWS services.

## Roadmap
Build a pipeline for:
- Data setup and storage (S3)
- Text extraction (Rekognition)
- Model training (IMDb dataset, SageMaker)
- App deployment
- ETL processes

## Projects
- **Data Setup**: Store IMDb dataset, mock sentiment data, and images in S3.
- **Text Extraction**: Use Rekognition for handwritten note analysis.
- **Model Training**: Train sentiment model on IMDb data.
- **App Deployment**: Deploy a web app for sentiment analysis.
- **Storage/ETL**: Process and store results in S3.

## Data Roles
- **IMDb Dataset**: Robust training for sentiment analysis.
- **Mock Sentiment**: Contextual stock sentiment data (AAPL, TSLA, MSFT, AMZN).

## Progress
- **Day 1**: Set up AWS account, created S3 bucket, generated `stocks_sentiment.csv` with `generate_mock_data.py`.

- Day 2: Fixed Rekognition parsing in `preprocess_data.py`. Addressed file naming inconsistency. Added `generate_rekognition.py`.
- Day 2: Trained BlazingText model in SageMaker Studio using `s3://market-analysis-tool/train/combined.csv`. Output saved to `s3://market-analysis-tool/output/`. Added `train_sagemaker.py` to repository.


