#!/usr/bin/env python
import yaml, sys

from sense_hat import SenseHat
import thingspeak

# API configuration
configuration_file = "config.yaml"

try:
  with open(configuration_file, 'r') as stream:
    try:
      config = yaml.load(stream)
    except yaml.YAMLError as error:
      sys.exit(error)
except Exception as ex:
  sys.exit(ex)

thingspeak_channel = config['thingspeak']['channel']
thingspeak_write_key = config['thingspeak']['write_key']

sense = SenseHat()

temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

channel = thingspeak.Channel(id=thingspeak_channel,write_key=thingspeak_write_key)
channel.update(thingspeak_channel, {1: temperature, 2: humidity, 3: pressure})
