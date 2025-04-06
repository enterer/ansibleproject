from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.securedb
collection = db.messages

@app.route("/")
def index():
    messages = collection.find()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", messages=messages, deployed_at=timestamp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
