import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
# Init 
    def __init__(self):

        # Enter your own keys here
        consumer_key = "wXXXXXXXXXXXXXXXXXXXXXXX1"
        consumer_secret = "qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXh"
        access_token = "9XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi"
        access_token_secret = "kXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXT"

        # Attempt authentication
        try:
            # Create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # Set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # Create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)

        # Added this, not sure if it was a temporary issue with Twitter, but for some reason my authentication failed sometimes
        except:
            print("Error: Authentication Failed")

 # Used to clean tweet text by removing links, special characters
    def clean_tweet(self, tweet):

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# Function to classify sentiment of passed tweet using textblob's sentiment method
    def get_tweet_sentiment(self, tweet):

        # Create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))

        # Set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        else:
            return 'negative'

# Main function to fetch tweets and parse them.
    def get_tweets(self, query, count=10):

        # Empty list to store parsed tweets
        tweets = []

        try:
            # Call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)

            # Parsing tweets one by one
            for tweet in fetched_tweets:
                # Empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # Saving text of tweet
                parsed_tweet['text'] = tweet.text
                # Saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # Appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # If tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # Return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any, not saying it won't happen, but just incase)
            print("Error : " + str(e))


def main():
    # Creating object of TwitterClient Class
    api = TwitterClient()
    # Calling function to get tweets
    tweets = api.get_tweets(query='Donald Trump', count=200)

    # Picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # Percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # Picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # Percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))

    # Printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # Printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])


if __name__ == "__main__":
    # Calling main function
    main()
