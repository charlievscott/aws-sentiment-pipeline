import sagemaker
from sagemaker import get_execution_role
import boto3
import time

# Initialize SageMaker session and role
sagemaker_session = sagemaker.Session()
role = get_execution_role()
region = boto3.Session().region_name

# Define S3 paths
bucket = 'market-analysis-tool'
input_prefix = 'train/combined.csv'
output_prefix = 'output'

# Specify BlazingText container
container = sagemaker.image_uris.retrieve('blazingtext', region)

# Configure the estimator
estimator = sagemaker.estimator.Estimator(
    container,
    role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=f's3://{bucket}/{output_prefix}/',
    sagemaker_session=sagemaker_session
)

# Set hyperparameters for BlazingText
estimator.set_hyperparameters(
    mode='supervised',  # Text classification
    epochs=10,
    learning_rate=0.05,
    min_count=5,
    word_ngrams=2,
    vector_dim=100
)

# Define input data
train_data = sagemaker.inputs.TrainingInput(
    s3_data=f's3://{bucket}/{input_prefix}',
    content_type='text/csv'
)

# Start training
job_name = f'blazingtext-{int(time.time())}'
estimator.fit({'train': train_data}, job_name=job_name)

# Print model output location
print(f'Model artifacts saved to: s3://{bucket}/{output_prefix}/{job_name}/output/')
