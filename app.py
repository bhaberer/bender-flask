import flask
import logging
import time
import json

from plugins.bender import bender

app = flask.Flask(__name__)

@app.route('/status')
def status():
  return 'I am alive!', 200


@app.route('/pax/<paxtype>')
def time_till_next_pax(paxtype):
  if paxtype:
    pax = bender.next_pax_for(paxtype)
  else:
    pax = bender.next_pax()

  return flask.jsonify({'text': pax.countdown_text()})

app.run(debug=True)
