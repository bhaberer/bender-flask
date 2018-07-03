import flask
import logging
import time
import json

from plugins.bender import bender

app = flask.Flask(__name__)

@app.route('/status')
def status():
  return 'I am alive!', 200


@app.route('/pax')
def next_pax():
  return flask.jsonify(bender.PAXES)

app.run
