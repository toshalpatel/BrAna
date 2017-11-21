# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Specifying the brand details
brand = "Apple"
filename = "tweets_apple.txt"

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '906776625932410881-eObfTfRaV6rRO1CK78ipjUZt5W2TFRV'
ACCESS_SECRET = 'A4BM1OFhYCkJgi6LubbD4I95cjltPbpG1zyYAdaEX5QAx'
CONSUMER_KEY = 'tC3spu2BsCON7qTe7jXL0adYO'
CONSUMER_SECRET = 'CnmhWML4XfQ7Qk78NYMhu9j0fEs6bwsbXjczgPPUuKEh7kkl0k'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track=brand, language="en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer.
tweet_count = 1000
print ("Brand: "+brand)
print ("Extract tweets..")
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #print(json.dumps(tweet))
    #json.dump(tweet, fhandle)
    tweet = json.dumps(tweet)
    dic_res = json.loads(tweet)
    d=dic_res['text']
    #print(d)
    with open('tweets_apple.txt','a',encoding='utf8') as f:
        f.write(d)
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break

f.close()
print("\n\n1000 tweets extracted")
