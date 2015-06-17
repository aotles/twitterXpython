import tweepy

def authenticate():
	consumer_key="XXXXXX"
	consumer_secret="XXXXXX"
	access_token="XXXXXX"
	access_token_secret="XXXXXX"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

def addOne(n):
	n = n + 1
	return n

def outputTweets(api, user, outputFile):
	tweets = ''
	public_tweets = api.user_timeline(count = 200, id = '@' + user)
	for tweet in public_tweets:
		try:
			outputFile.write(tweet.text + '\n' + '\n') 
		except UnicodeEncodeError:
			outputFile.write('[#]') 
	return public_tweets

def sendTweet(api, message):
	api.update_status(status = message)

