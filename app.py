import flask
from flask import request
import logging
import time

app = flask.Flask(__name__)

@app.route('/')
def success():
  return 'I am a success!', 200

app.run(debug=True, host='0.0.0.0', port=80)
