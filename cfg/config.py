
class Config(object):
  # Map DataPoint data streams to cosm feeds:
  idigi_in = {
    # upstairs XBee Sensor L/T
    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_4062A568/AD1": {
        "cosm_datastream": "upstairs_light",                # Cosm datastream
        "f(x)": "float('%.1f' % (int(x) / 1023.0 * 1200))"  # apply Python expression to data
    },
  }

  cosm_out = {
    "api_key": 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'feed_id': 12343,
  }

