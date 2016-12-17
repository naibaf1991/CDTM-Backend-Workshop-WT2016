#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file, jsonify
import sys
from task import Task as Task
from list import List as List

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

myList = List(0, 'Inbox')
myTasks = [
    Task('Think about lunch', '0', id='0', status = Task.COMPLETED),
    Task('Become a pro in backend development', '0', status= Task.NORMAL),
    Task('CONQUER THE WORLD!', '0', status = Task.NORMAL)
]


VERSION = 2.0

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify({'version':VERSION})

@app.route('/api/lists/', methods=['GET'])
def apilists():
    return jsonify({'lists':myList.jsonreturnList()})

@app.route('/api/lists/:id/tasks', methods=['GET'])
def apilisttasks():
    output = []
    for tasks in myTasks:
        output.append(tasks.__dict__)
    return jsonify({'tasks':output})

@app.route('/api/lists/<int:idlist>/tasks')
def apilistspecial(idlist):
    output = []
    for tasks in myTasks:
        if myTasks.index(tasks) == idlist:
            output.append(tasks.__dict__)
    return jsonify({'tasks':output})

@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)



