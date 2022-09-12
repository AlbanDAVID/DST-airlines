import pandas as pd
import static

import boto3
s3_client = boto3.client('s3', aws_access_key_id= static.aws_access_key_id , aws_secret_access_key= static.aws_secret_access_key)

import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient(static.cnx_mongodb, tlsCAFile=ca)

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
    
