import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "rishu567-demo"
PREFIX = "RawData/"

def list_s3_files():
    try:
        s3 = boto3.client("s3")
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)
        files = response.get("Contents", [])
        if not files:
            print(f"No files found in {PREFIX}")
            return
        print(f"Files in s3://{BUCKET_NAME}/{PREFIX}")
        for file in files:
            print(f"File: {file['Key']} | Size: {file['Size']} bytes")
    except ClientError as error:
         print(f"File: {file['Key']} | Size: {file['Size']} bytes")
    except ClientError as error:
        print("AWS error:", error)

if __name__ == "__main__":
    list_s3_files()
