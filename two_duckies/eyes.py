#!/usr/bin/env python
import yaml, sys

from time import sleep
import tweepy, webbrowser
from picamera import PiCamera

# API configuration
configuration_file = "config.yaml"
credentials_file = "credentials.yaml"

try:
  with open(configuration_file, 'r') as stream:
    try:
      config = yaml.load(stream)
    except yaml.YAMLError as error:
      sys.exit(error)
except Exception as ex:
  sys.exit(ex)

twitter_api_key = config['twitter']['api_key']
twitter_api_secret = config['twitter']['api_secret']

# Auth Redirection
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)

# Use (set) stored access token if available
try:
  with open(credentials_file, "r") as stream:
    try:
      credentials = yaml.load(stream)
      auth.set_access_token(credentials['token'], credentials['token_secret'])
    except yaml.YAMLError as error:
      sys.exit(error)
except FileNotFoundError:
  # Do the OAuth dance is credentials are not available
  try:
    redirect_url = auth.get_authorization_url()
  except tweepy.TweepError as ex:
    print("Error! Failed to get request token.")
    sys.exit(ex)
  if webbrowser.open(redirect_url,new=2):
    print("A browser window will appear to authorize. You can also access directly: "+redirect_url)
  else:
    print("Open the following URL in a browser to authorize: "+redirect_url)
  
  # Verification
  verifier = input('Please enter the verifier from the Twitter page (once you authorize the application):').strip()
  try:
    auth.get_access_token(verifier)
  except tweepy.TweepError:
    print("Error! Failed to get access token.")
    sys.exit(ex)

  # Save access token
  credentials = {'token': auth.access_token, 'token_secret': auth.access_token_secret}
  with open(credentials_file, "w") as file:
    yaml.dump(credentials, file, default_flow_style=False)

# Initialize camera
camera = PiCamera()

# Let's go!
twitter_api = tweepy.API(auth)

camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)

camera.capture('/tmp/capture.jpg')
sleep(2)

twitter_api.update_with_media('/tmp/capture.jpg')
