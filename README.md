# AWS Secure S3 Data Engineering Project

## Objective
Built a secure AWS S3 storage workflow using EC2, IAM roles, Python, and Boto3.

## AWS Services
- Amazon S3
- Amazon EC2
- AWS IAM

## Project Features
- Stored CSV data in the S3 RawData/ prefix.
- Used an EC2 IAM role for AWS access without hardcoded credentials.
- Listed S3 objects using Python and Boto3.
- Restricted the IAM policy to the rishu567-demo bucket.
- Enabled S3 Block Public Access.
- Configured SSE-S3 default encryption.
- Added a bucket policy denying insecure HTTP transport.

## Validation
- Successfully ran s3_list_files.py from EC2.
- Downloaded RawData/customers.csv from S3.
- Processed 5 CSV rows with process_customers.py, removing surrounding whitespace and skipping blank rows.
- Uploaded the cleaned output to Processed-data/customers_cleaned.csv.
- Added .gitignore rules to keep local customer data and processed files out of Git.
- Confirmed RawData/customers.csv was listed (138 bytes).
- Python syntax check passed.

## Security Notes
- S3 Block Public Access is enabled.
- Object Ownership is Bucket owner enforced.
- Default encryption uses SSE-S3.
- IAM policy grants ListBucket, GetObject, and PutObject on the specified bucket.
- Review all attached policies periodically to confirm effective permissions.

## Future Improvements
- Upgrade the Python environment to a supported version.
- Add stronger CSV validation and data-quality checks.
- Add automated logging and error handling.
