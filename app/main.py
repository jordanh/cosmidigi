#!/usr/bin/env python

import sys,os
import logging
import json
import numbers
from bottle import route, get, post, put, run, request, response

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cfg.config import Config
from simplecosm import SimpleCosm


# setup logging:
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


@route("/")
def main():
  return "Hello, world."

@put("/idigi")
def main():
  log = logging.getLogger("idigi.PUT")
  log.setLevel(logging.DEBUG)
  log.info("iDigi PUT")
  idigi_put = json.load(request.body)
  if "Document" not in idigi_put:
    log.warning("Document not found in json payload")
    return
  if "Msg" not in idigi_put["Document"]:
    log.warning("Msg not found in json payload")
    return
  msgs = idigi_put["Document"]["Msg"]
  if isinstance(msgs, dict):
    msgs = (msgs,)

  cosm = SimpleCosm(Config.cosm_out['feed_id'], Config.cosm_out['api_key'])

  for msg in msgs:
    if 'DataPoint' not in msg:
      continue
    dp = msg['DataPoint']
    if dp['streamId'] not in Config.idigi_in:
      log.debug("no matching idigi_in config found")
      continue
    cfg_in = Config.idigi_in[dp['streamId']]
    data = dp['data']
    if isinstance(data,numbers.Number):
      if 'f(x)' in cfg_in:
        try:
          data = eval(cfg_in['f(x)'],{'x': data})
        except Exception, e:
          log.warning("f(%s) = %s eval exc %s" % (repr(data),cfg_in['f(x)'], str(e)))
    cosm.append_data(cfg_in["cosm_datastream"], data)
    log.info("COSM out %s -> %s" % (repr(data), cfg_in["cosm_datastream"]))

  cosm.put()  

if __name__ == "__main__":
  run(host="0.0.0.0", port=8080, debug=True)

