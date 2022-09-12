import certifi
import pymongo
from pymongo import MongoClient
from read_file_from_s3 import read_latest_file
import static

def add_data_collection(folder,collection):
    ca = certifi.where()
    client = MongoClient(static.cnx_mongodb, tlsCAFile=ca)
    data = read_latest_file('datalake-airlines', folder)

    db = client['data_airlines']
    col = db[collection]
    col.delete_many({})
    col.insert_many(data)