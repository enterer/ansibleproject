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
    
    # Read timestamp from log
    try:
        with open("deploy.log", "r") as f:
            last_deployed = f.read().strip()
    except FileNotFoundError:
        last_deployed = "Unknown"

    return render_template("index.html", messages=messages, last_deployed=last_deployed)

# Write current timestamp to log when app starts
with open("deploy.log", "w") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
