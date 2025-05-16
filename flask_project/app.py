from flask import Flask
import json

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


if __name__ == '__main__':
  app.run(debug=True)

  