# AWS Secure S3 Data Engineering Project

## Objective
Build a secure AWS S3 storage workflow using IAM least-privilege access and encrypted data storage.

## AWS Services
- Amazon S3
- AWS IAM
- Amazon EC2

## S3 Bucket Structure
- RawData/ — stores original CSV files
- Processed-data/ — for processed files
- Archive/ — for archived files

## Security
- IAM role for EC2 access
- Restricted S3 permissions
- Deny insecure HTTP transport
- S3 Block Public Access and encryption settings to be verified

## Current Progress
- Created S3 bucket and folders
- Uploaded customers.csv to RawData/
- Created IAM policy and EC2 role
- Launched EC2 and installed Python and Git

## Verified Progress
- Installed boto3 in the EC2 Python environment.
- Created `s3_list_files.py` to list objects under `RawData/`.
- Successfully ran the script from EC2 and confirmed `RawData/customers.csv` is listed (138 bytes).
- Python syntax check passed using `python3 -m py_compile s3_list_files.py`.

## Notes
- S3 bucket security settings, encryption, and least-privilege permissions still need verification.
- Python 3.9 shows a Boto3 deprecation warning; consider upgrading to Python 3.10 or later.
