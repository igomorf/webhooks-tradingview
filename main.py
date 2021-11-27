import os
from flask import Flask, request, abort, json
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return "<h1>Olá Mundo!</h1>"

@app.route("/webhook", methods=['GET'])
def deploy():
    return "<h1>Testando deploy do webhook!</h1>"

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

# @app.route("/webhook", methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         print(request.json)
#         return 'success', 200
#     else:
#         abort(400)

if __name__  == '__main__':
    app.run(debug=True)

