import boto3
from botocore.exceptions import ClientError

# Initialize S3 client with a region of choice
def get_s3_client(region='us-east-1'):
    return boto3.client('s3', region_name=region)

def create_s3_bucket(s3_client, bucket_name, region='us-east-1'):
    """Create an S3 bucket."""
    try:
        if region == 'us-east-1':
            # 'us-east-1' region doesn't need LocationConstraint
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # For other regions, specify the LocationConstraint
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' created successfully!")
        return bucket_name
    except ClientError as e:
        print(f"Error creating bucket {bucket_name}: {e}")
        return None

def upload_car_image(s3_client, bucket_name, image_name, file_path):
    """Upload a car image to the S3 bucket."""
    try:
        s3_client.upload_file(file_path, bucket_name, image_name)
        print(f"File '{image_name}' uploaded to bucket '{bucket_name}' successfully!")
    except ClientError as e:
        print(f"Error uploading file {image_name} to bucket {bucket_name}: {e}")

# Usage Example
region = 'us-east-1'  # You can change the region if needed
bucket_name = 'car-images-bucket'
s3_client = get_s3_client(region)

# Create the S3 bucket
bucket_name = create_s3_bucket(s3_client, bucket_name, region)

# Upload a car image if the bucket was created successfully
if bucket_name:
    upload_car_image(s3_client, bucket_name, 'toyota_camry.jpg', '/path/to/toyota_camry.jpg')
import boto3
from botocore.exceptions import ClientError

# Initialize S3 client
def get_s3_client(region=None):
    if region is None:
        return boto3.client('s3')
    return boto3.client('s3', region_name=region)

def create_bucket(s3_client, bucket_name, region=None):
    """Create an S3 bucket if it doesn't exist."""
    try:
        # Check if the bucket already exists
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
        return bucket_name
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            # Bucket doesn't exist; create it
            if region is None or region == 'us-east-1':
                # 'us-east-1' does not need a LocationConstraint
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                # Other regions require a LocationConstraint
                s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={
                        'LocationConstraint': region
                    }
                )
            print(f"Bucket '{bucket_name}' created successfully.")
            return bucket_name
        else:
            # Other errors
            print(f"Error checking bucket: {e.response['Error']['Message']}")
            return None

def upload_car_image(s3_client, bucket_name, image_name, file_path):
    """Upload a car image to the S3 bucket."""
    try:
        s3_client.upload_file(file_path, bucket_name, image_name)
        print(f"File '{image_name}' uploaded to bucket '{bucket_name}' successfully.")
    except ClientError as e:
        print(f"Error uploading file '{image_name}' to bucket '{bucket_name}': {e.response['Error']['Message']}")

# Usage Example
region = 'us-east-1'  # Specify your desired region
bucket_name = "vehicle-maintenance-reports-folder"
image_name = 'toyota_camry.jpg'
file_path = '"C:\\Users\\saira\\Downloads\\car.jpg"'

# Initialize S3 client
s3_client = get_s3_client(region)

# Create the bucket if it doesn't exist
bucket_name = create_bucket(s3_client, bucket_name, region)

# Upload an image if the bucket exists or was created successfully
if bucket_name:
    upload_car_image(s3_client, bucket_name, image_name, file_path)
