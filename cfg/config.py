
class Config(object):
  idigi_in = {
    # upstairs XBee Sensor L/T
    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_4062A568/AD1": {
        "cosm_datastream": "upstairs_light",
        "f(x)": "float('%.1f' % (int(x) / 1023.0 * 1200))"
    },

    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_4062A568/AD2": {
        "cosm_datastream": "upstairs_temperature",
        "f(x)": "float('%.1f' % ((int(x) / 1023.0 * 1200 - 500) / 10.0))",
    },
    # downstairs XBee Sensor L/T/H
    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_406F7C67/AD1": {
        "cosm_datastream": "downstairs_light",
        "f(x)": "float('%.1f' % (int(x) / 1023.0 * 1200))"
    },

    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_406F7C67/AD2": {
        "cosm_datastream": "downstairs_temperature",
        "f(x)": "float('%.1f' % ((int(x) / 1023.0 * 1200 - 500) / 10.0))",
    },

    "dia/channel/00000000-00000000-00409DFF-FF43FA07/XBee_406F7C67/AD3": {
        "cosm_datastream": "downstairs_humidity",
        "f(x)": "float('%.1f' % ((int(x) / 1023.0 * 1200 * 108.2 / 33.2 / 5000 - 0.16) / 0.0062))",
    },
  }

  cosm_out = {
    "api_key": 'xTGZda731wqijtX9QyBVN7JJ3ASSAKxNdnZzdTlhakp1Zz0g',
    'feed_id': 95223,
  }

