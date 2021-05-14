from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import pandas as pd
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'bookuser-db'
app.config["MONGO_URI"] = "mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/book-recommender?retryWrites=true&w=majority"
mongo = PyMongo(app)
books = pd.read_csv('books.csv') 
books_book_conv = {m : m-1 for m in books['book_id'] }
books['book_id'] = books['book_id'].apply(lambda m: books_book_conv[m])
books.drop(columns=['goodreads_book_id', 'best_book_id', 'work_id', 'books_count', 'isbn','isbn13','original_publication_year','original_title','language_code','average_rating','ratings_count','work_ratings_count','work_text_reviews_count','ratings_1','ratings_2','ratings_3','ratings_4','ratings_5','small_image_url'])
print(books)
books_dict = books.to_dict('records')
print(book_dict)
client = pymongo.MongoClient("mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/book-recommender?retryWrites=true&w=majority")
db = client["book-recommender"]
book_collect = db["book-data"]
#book_collect.insert_many(books_dict, ordered=False)