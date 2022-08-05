import certifi
import pymongo
from pymongo import MongoClient
from read_file_from_s3 import read_latest_file

def add_data_collection(folder,collection):
    ca = certifi.where()
    client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
    data = read_latest_file('datalake-airlines', folder)

    db = client['data_airlines']
    col = db[collection]
    col.delete_many({})
    col.insert_many(data)