"""Flaskフレームワークによる単純なサーバーでも
"""
# Standard
import os

# 3rdParty
import flask

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
app = flask.Flask('app server')

@app.route('/')
def index():
    return 'hello Dockerfile'

# run application 
app.run(debug=True, host=HOST, port=PORT)

