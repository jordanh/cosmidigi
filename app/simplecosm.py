import logging
import json
import requests

log = logging.getLogger("cosm")

class SimpleCosm:
  _url_base = "http://api.pachube.com/v2/feeds/"

  def __init__(self, feed_id, api_key):
    self._version = "1.0.0"
    self._feed_id = str(feed_id)
    self._headers = { 'X-PachubeApiKey': api_key }
    self._data = []

  def append_data(self, datastream_id, dp_value):
    self._data.append({'id': datastream_id, 'current_value': dp_value})
    log.debug("added sample to %s" % repr(datastream_id))

  def put(self):
    url = SimpleCosm._url_base + self._feed_id + "?_method=put"
    payload = {
      'version': self._version,
      'id': self._feed_id,
      'datastreams': self._data,
    }
    r = requests.put(url, data=json.dumps(payload), headers=self._headers)
    log.info("PUT to Cosm result %d" % r.status_code)
    if r.status_code == requests.codes.ok:
      self._data = []
    
    return r.status_code

