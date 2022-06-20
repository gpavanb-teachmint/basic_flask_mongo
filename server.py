from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://root:example@localhost:27018')
db = client.local


# basic route
@app.route('/')
def hello_world():
    data = db.data.find_one({"_id": "1"})
    return data['value']
  
# main driver function
if __name__ == '__main__':
    app.run()