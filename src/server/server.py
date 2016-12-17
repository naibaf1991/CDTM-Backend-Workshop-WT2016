#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file
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
    Task('Think about lunch', '0', id=myList.id, status=Task.COMPLETED),
    Task('Become a pro in backend development', id=myList.id, status=Task.NORMAL),
    Task('CONQUER THE WORLD!', id=myList.id, status=Task.NORMAL)
]


@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')

@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)



