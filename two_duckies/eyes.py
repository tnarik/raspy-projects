#!/usr/bin/env python
import yaml, sys

from time import sleep
import tweepy, webbrowser
from picamera import PiCamera

# API configuration
configuration_file = "config.yaml"
credentials_file = "creds.csv"

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

camera = PiCamera()

# Auth Redirection
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)

# Use (set) stored access token if available
try:
  with open(credentials_file, "r") as f:
    access_token=f.readline().strip()
    access_token_secret=f.readline().strip()
    auth.set_access_token(access_token, access_token_secret)
except FileNotFoundError:
  # Do the OAuth dance is credentials are not available
  try:
    redirect_url = auth.get_authorization_url()
  except tweepy.TweepError as ex:
    print("Error! Failed to get request token.")
    sys.exit(ex)
  print(redirect_url)
  webbrowser.open(redirect_url,new=2)
  
  # Verification
  verifier = input('Please type the verifier from the Twitter page (once you authorize the application):').strip()
  try:
    auth.get_access_token(verifier)
  except tweepy.TweepError:
    print("Error! Failed to get access token.")
    sys.exit(ex)

  # Save access token
  with open(credentials_file, "w") as f:
    print(auth.access_token, file=f)
    print(auth.access_token_secret, file=f)


# Let's go!
api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#  print("- "+tweet.text)

camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('/tmp/capture.jpg')
sleep(2)
