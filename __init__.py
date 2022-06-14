from flask import Flask, jsonify, request
import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

port = 8080

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

@app.route('/', methods=['GET','POST'])
def mainPage():
    data = "This is a data"
    return jsonify({'data': data})


@app.route('/get-port')
def getPort():
    return jsonify({'port' : port})

if __name__ == '__main__':
    app.run(port=port)