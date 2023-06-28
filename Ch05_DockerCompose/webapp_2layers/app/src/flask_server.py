"""Flaskフレームワークによる単純なサーバーでも
"""
# Standard
import os

# 3rdParty
import flask

PORT = int(os.environ['PORT'])
app = flask.Flask('app server')

@app.route('/')
def route_index():
    return 'hello Dockerfile on ch05'

@app.route('/api/v1/hello')
def api_index():
    return 'hello api v1 Dockerfile on ch05'

# run application 
app.run(debug=True, host="0.0.0.0", port=PORT)

