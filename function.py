import tweepy

def authenticate():
	consumer_key="m5Gp6Dsn0XSOoLDDiuM7YWjvg"
	consumer_secret="jcGeb8P1g3nWpBWBx5XNtGw6m2QLCrJidfk7r8Kdj36gf67u1g"
	access_token="916209919-kNU2JFW6MGA9UscJRQ3u91Gcn409anMhoXvgwO1M"
	access_token_secret="VIYiNfjIa6xBNrePgxStoFEHxZC39QYh7ycCHgxVkGbUr"
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

