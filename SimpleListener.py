import json

import tweepy


class SimpleListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status):
        print status
