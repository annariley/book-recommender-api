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
api = Api(app)
mongo = PyMongo(app)


client = pymongo.MongoClient("mongodb+srv://dbUser:cpen291@cluster0.02dfd.mongodb.net/book-recommender?retryWrites=true&w=majority")
db = client["book-recommender"]
collection = db["user-data"]
db.collection.insert_one({"_id":0,
"book 1 id": 1234,"book 1 rating": 4,
"book 2 id": 5678,"book 2 rating": 2, 
"book 3 id": 9101,"book 3 rating": 5,
"book 4 id": 1121,"book 4 rating": 1,
"book 5 id": 3141,"book 5 rating": 4})

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("books", type=list, help="The initial 5 book id / rating tuples", required=True)

def abort_if_id_dne(user_id):
    if user_id not in users:
        abort(404, message="Could not find user")

def abort_if_id_exists(user_id):
    if user_id in users:
        abort(409, message="User already exists")

class User(Resource):
    def get(self, user_id):
        abort_if_id_dne(user_id)
        #get a book rec from back end and return the book id
        return users[user_id]

    def put(self, user_id):
        args = user_put_args.parse_args()
        #args should be a list of book id/rating tuples for a specific user
        #we gotta send it to backend/store it on the cloud/ use it to find similar user to initialize embedding model
        db = client['bookuser-db']
        my_col = db['users']
        return {user_id: args}



if __name__ == "__main__":
    app.run(debug=True)