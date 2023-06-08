import time
from flask import Flask, request, redirect
from flask.helpers import make_response
from flask.json import jsonify

app = Flask(__name__)
from flask import Flask, request, redirect

@app.route('/timeout')
def should_return_after_sixty_seconds():
  time.sleep(80)
  return make_response(jsonify({"success":True}))
