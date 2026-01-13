import logging
import boto3
from botocore.exceptions import ClientError
import json

# You can change this params
service_name = 's3'
endpoint_url = 'https://storage.yandexcloud.net'
access_key = 'your-access-key'
secret_key = 'your-secret-key'
region_name = 'ru-central1'
bucket_name = "your-bucket-name"
object_name = "file-name.txt"
max_size = 5 * 1024 * 1024  # Max file-size in bytes
expiration = 3600           # Lifetime in seconds

def create_presigned_post(fields=None):

    conditions = [["content-length-range", 1, max_size]]

    session = boto3.session.Session()
    s3_client = session.client(
        service_name=service_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region_name
    )

    try:
        response = s3_client.generate_presigned_post(
            bucket_name,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None

    return response


if __name__ == "__main__":
    response = create_presigned_post()

    print("PRE-signed URL:")
    print(json.dumps(response, indent=4))
