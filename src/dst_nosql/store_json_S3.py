from datetime import datetime
import boto3


def upload_file_airlabs(bucket, folder, prefix, file_to_upload):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW',
                             aws_secret_access_key='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')

    now = datetime.now()
    file_name = prefix + "_" + now.strftime("%d%m%Y_%H%M%S") + ".json"

    key = folder + "/" + file_name
    try:
        response = s3_client.upload_file(file_to_upload, bucket, key)
    except FileNotFoundError as e:
        print(e)
        return False
    return True