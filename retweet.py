#!/usr/bin/python

import tweepy

from ConfigUtils import ConfigUtils
from SimpleListener import SimpleListener


config_utils = ConfigUtils()

# # config values
# settings
search_query = config_utils.read_list("settings", "search_query")
tweet_languages = config_utils.read_list("settings", "tweet_language")
userBlacklist = config_utils.read_list("settings", "userBlacklist")
wordBlacklist = config_utils.read_list("settings", "wordBlacklist")
# twitter
consumer_key = config_utils.get("twitter", "consumer_key")
consumer_secret = config_utils.get("twitter", "consumer_secret")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token = config_utils.get("twitter", "access_token")
access_token_secret = config_utils.get("twitter", "access_token_secret")

print ''
# create bot
auth.set_access_token(access_token, access_token_secret)
listener = SimpleListener()
stream = tweepy.Stream(auth, listener)
stream.filter(track=search_query)

