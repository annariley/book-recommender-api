from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

db = client["book-recommender"]
collect = db["user-data"]

#collect.insert_one({"_id":0,
#"book 1 id": 1234,"book 1 rating": 4,
#"book 2 id": 5678,"book 2 rating": 2, 
#"book 3 id": 9101,"book 3 rating": 5,
#"book 4 id": 1121,"book 4 rating": 1,
#"book 5 id": 3141,"book 5 rating": 4})

collect.delete_one({"_id":0})
