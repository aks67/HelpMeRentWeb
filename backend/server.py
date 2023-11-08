from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

global budget

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mainPage')
def get_landing_page():
    pass    


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
