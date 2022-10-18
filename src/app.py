import flask
import json
from flask import request
from flask import Flask,jsonify
app = Flask(__name__)

todos = [{ "label": "My first task", "done": False },{ "label": "My second task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = flask.jsonify(todos)
    print(json_text)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = flask.jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    json_text = flask.jsonify(todos)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)