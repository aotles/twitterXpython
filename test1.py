from __future__ import absolute_import, print_function
 
import tweepy
 
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.
 
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="XXXX"
consumer_secret="XXXX"
 
# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="XXXX"
access_token_secret="XXXXX"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)
 
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
# n = 1
single_tweet = '?.??.??.?'
api.update_status(status = single_tweet)
# for n in range(1,101):
# 	single_tweet = 'BADGERS ' + str(n)
# 	api.update_status(status = single_tweet)
# single_tweet = str('All done! Thanks for your patience everyone!')
# api.update_status(status = single_tweet) s s dfsdf
#tesst