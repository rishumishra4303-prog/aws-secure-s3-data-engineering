import csv
import os

BASE_DIR = "/home/ec2-user/aws-data-engineer-project"
INPUT_FILE = os.path.join(BASE_DIR, "customers.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "processed")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "customers_cleaned.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    if not reader.fieldnames:
        raise ValueError("CSV header missing")
    rows = [{k: (v.strip() if v else "") for k, v in row.items()} for row in reader]
    rows = [row for row in rows if any(row.values())]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Rows processed:", len(rows))
print("Saved:", OUTPUT_FILE)
