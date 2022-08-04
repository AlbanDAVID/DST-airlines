import boto3


def download_latest_file(bucket, folder):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=folder)
    objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])
    latest_object = objects[-1]['Key']
    filename = latest_object[latest_object.rfind('/')+1:]
    s3_client.download_file('datalake-airlines', latest_object, filename)

#Exemple d'utilisation : download_latest_file("datalake-airlines","01-flights-json/")


def download_all_files(bucket, folder):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=folder)
    objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])
    print(len(objects))
    for i in range (1,len(objects)):
        latest_object = objects[i]['Key']
        filename = latest_object[latest_object.rfind('/')+1:]
        s3_client.download_file(bucket, latest_object, filename)

def download_all_files_by_date(bucket, folder,prefix,day,month,year):
    s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=folder+prefix+day+month+year)
    objects = sorted(response['Contents'], key=lambda obj: obj['LastModified'])
    print(len(objects),"files found")
    for i in range (1,len(objects)):
        latest_object = objects[i]['Key']
        filename = latest_object[latest_object.rfind('/')+1:]
        s3_client.download_file(bucket, latest_object, filename)