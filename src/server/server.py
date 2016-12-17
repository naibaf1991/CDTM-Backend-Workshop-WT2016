#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file
import sys
import task
import list

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



if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
    l1 = list(0,'Inbox')
    t1 = ([task(0,'maxi_depp', l1,'normal','boring','heute',1),task(1,'maxi_depp2',l1,'completed','exciting','13.01.',1)])


