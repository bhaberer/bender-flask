import flask
from flask import request
import logging
import time

@app.route('/')
def success():
  return 'I am a success!', 200
