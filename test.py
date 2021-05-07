import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "user/" + "2", {"_id":2,
"book 1 id": 1111,"book 1 rating": 5,
"book 2 id": 2222,"book 2 rating": 5, 
"book 3 id": 3333,"book 3 rating": 5,
"book 4 id": 4444,"book 4 rating": 1,
"book 5 id": 5555,"book 5 rating": 5})

#resp1 = requests.delete(BASE + "user/" + "1")
#resp2 = requests.delete(BASE + "user/" + "2")
