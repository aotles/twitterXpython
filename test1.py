from __future__ import absolute_import, print_function
 
import tweepy, function

api = function.authenticate()
outputFile = open('outputFile', 'w')
user = api.me().name
outputFile.write( user + '\n' + '\n')

user = 'rocketpope'
myTweets = function.outputTweets(api, user, outputFile)
