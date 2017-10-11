import re
import json
import urllib

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/view", methods=['POST'])
def view():
    if request.method == 'POST':
        data = request.get_json()
        url = urllib.parse.quote_plus(data['url'])
        with open('./data/%s.json'%(url), 'w') as f:
            f.write(json.dumps({"body": data['body'], "url": data['url']}, ensure_ascii=False))
    return data['url']

if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'server.key'))
