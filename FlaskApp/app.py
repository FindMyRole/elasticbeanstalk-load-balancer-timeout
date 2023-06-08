def local_deps():
  import sys
  if sys.platform == 'win32':
    sys.path.append(sys.path[0] + '\site-packages\windows')
  elif sys.platform =='linux':
    sys.path.append(sys.path[0] + './site-packages/linux')
  elif sys.platform =='darwin':
    sys.path.append(sys.path[0] + './site-packages/linux')

local_deps()
import time
from flask import Flask, request, redirect
from flask.helpers import make_response
from flask.json import jsonify

app = Flask(__name__)

@app.route('/timeout')
def should_return_after_sixty_seconds():
  time.sleep(80)
  return make_response(jsonify({"success":True}))


@app.route('/',methods=['GET'])
def healthcheck():
  return {
    "msg":"A-OK"
  },200


if __name__ == "__main__":
  app.run()
