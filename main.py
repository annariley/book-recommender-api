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
user_put_args.add_argument("user id", type=int, help = "user id required", required=True)
user_put_args.add_argument("book 1 id", type=int, help="book 1 id required", required=True)
user_put_args.add_argument("book 1 rating", type=int, help="book 1 rating required", required=True)
user_put_args.add_argument("book 2 id", type=int, help="book 2 id required", required=True)
user_put_args.add_argument("book 2 rating", type=int, help="book 2 rating required", required=True)
user_put_args.add_argument("book 3 id", type=int, help="book 3 id required", required=True)
user_put_args.add_argument("book 3 rating", type=int, help="book 3 rating required", required=True)
user_put_args.add_argument("book 4 id", type=int, help="book 4 id required", required=True)
user_put_args.add_argument("book 4 rating", type=int, help="book 4 rating required", required=True)
user_put_args.add_argument("book 5 id", type=int, help="book 5 id required", required=True)
user_put_args.add_argument("book 5 rating", type=int, help="book 5 rating required", required=True)

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

    def put(self):
        args = user_put_args.parse_args()
        db = client["book-recommender"]
        collect = db["user-data"]
        abort_if_id_exists(args["user id"])
        collect.insert_one(args)
        #collect.insert_one({"_id":user_id,
        #"book 1 id": args["book 1 id"],"book 1 rating": args["book 1 rating"],
        #"book 2 id": args["book 1 id"],"book 2 rating": args["book 1 rating"],
        #"book 3 id": args["book 1 id"],"book 3 rating": args["book 1 rating"],
        #"book 4 id": args["book 1 id"],"book 4 rating": args["book 1 rating"],
        #"book 5 id": args["book 1 id"],"book 5 rating": args["book 1 rating"],})
        #args should be a list of book id/rating tuples for a specific user
        #we gotta send it to backend/store it on the cloud/ use it to find similar user to initialize embedding model
        return {"entry": args}, 201



if __name__ == "__main__":
    app.run(debug=True)