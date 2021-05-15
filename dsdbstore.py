import pandas as pd
import numpy as np
from torch import nn, optim
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bookuser-db'
app.config["MONGO_URI"] = "mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/book-recommender?retryWrites=true&w=majority"
mongo = PyMongo(app)
client = pymongo.MongoClient("mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/book-recommender?retryWrites=true&w=majority")
db = client["book-recommender"]
book_collect = db["book-data"]
print(book_collect.find_one({"book_id":1})["authors"])

#Not sure if the below code should stay here or be elsewhere. We will need wherever we train our models. Not sure if we need it in the backnd anymore, now that book info
#is in Mongo.