import pandas as pd

import boto3
s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')

import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

def get_aircrafts_preprocessed():
    db = client['data_airlines']
    try:
        col_fleets = db['fleet']
        df_fleets = pd.DataFrame(list(col_fleets.find()))
        df_fleets=df_fleets.dropna(subset=["hex"]).reset_index(drop=True)
        df_fleets=df_fleets.drop_duplicates(subset=['hex'], keep='first').reset_index(drop=True)
        df_fleets=df_fleets.iloc[:,1:]
        df_fleets.iloc[:,1:].fillna("To be defined", inplace = True)
        return df_fleets
    except:
        pass
    
df = get_aircrafts_preprocessed()
print(df)
