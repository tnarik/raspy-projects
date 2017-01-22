#!/usr/bin/env python
import unicornhat as unicorn
import socket
import urllib.request
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.4)

if '127.0.0.1' == socket.gethostbyname(socket.gethostname()):
  unicorn.set_pixel(0,0,255,0,0)
elif '127.0.1.1' == socket.gethostbyname(socket.gethostname()):
  unicorn.set_pixel(0,0,0,0,255)
else:
  unicorn.set_pixel(0,0,0,255,0)

print("Interface checked")

try:
  response = urllib.request.urlopen('http://www.google.com/')
  if 200 == response.code:
    print("Connection to Google checked")
    unicorn.set_pixel(1,0,0,255,0)
  else:
    print("Connection to Google wrong")
    unicorn.set_pixel(1,0,255,255,0)
except:
  print("Connection to Google failed")
  unicorn.set_pixel(1,0,255,0,0)

unicorn.show()

time.sleep(10)