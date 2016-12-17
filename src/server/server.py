#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file
import sys

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')


class List(object):
    def __init__(self,id,title,revision):
        self.id = id
        self.title = title
        self.revision = revision

class Task(object):
    def __init__(self,id,title,list,status,description,due,revision):
        self.id = id
        self.title = title
        self.list = list
        self.status = status
        self.description = description
        self.due = due
        self.revision = revision



if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
