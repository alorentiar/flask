from flask import Flask, jsonify, request
import json,logging

logging.basicConfig(filename='requests.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

app = Flask(__name__)

# Configuring JSON
# with open('details.json', 'r') as c:
#     userDetails = json.load(c)["users"]


@app.route('/submitdata', methods=['POST'])
def upload_file():
    print(request.json)
    logging.info("Request : ",request.json)

    return jsonify(request.json), 201


@app.route('/submitfile', methods=['POST'])
def upload_file():
    print(request.json)
    logging.info("Request : ",request.json)

    return jsonify(request.json), 201


if __name__ == '__main__':
    logging.info("Application Running")
    app.run(debug=True)