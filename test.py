import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "user/" + "1", {"_id":1,
"book 1 id": 1234,"book 1 rating": 4,
"book 2 id": 5678,"book 2 rating": 2, 
"book 3 id": 9101,"book 3 rating": 5,
"book 4 id": 1121,"book 4 rating": 1,
"book 5 id": 3141,"book 5 rating": 4})