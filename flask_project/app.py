from flask import Flask, request
import json, os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client.test 
collection = db.todo

app = Flask(__name__)
@app.route('/api')
def api():
  f = open('./flask_project/data.txt', 'r')
  data = f.read()
  f.close()
  # print(data)
  data = json.loads(data)
  data = {'data': data}
  return data

@app.route('/submittodoitem', methods=['POST'])
def submit():
  data = request.form
  data = dict(data)
  try:
    collection.insert_one(data)
  except:
    return "Error while submitting. Try again!"
  return "Data successfully submitted"

  
if __name__ == '__main__':
  app.run(debug=True)

  