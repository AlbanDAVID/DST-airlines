import boto3
import json
import static

def read_latest_file(bucket, folder, file_prefix=""):
    s3_client = boto3.client('s3', aws_access_key_id= static.aws_access_key_id,aws_secret_access_key=static.aws_secret_access_key)
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=folder+file_prefix)
    objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])
    latest_object = objects[-1]['Key']
    filename = latest_object[latest_object.rfind('/') + 1:]
    FILE_TO_READ = folder+filename
    result = s3_client.get_object(Bucket=bucket, Key=FILE_TO_READ)
    text = result["Body"].read().decode()
    json_content = json.loads(text)
    return json_content