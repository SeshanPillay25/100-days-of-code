
import tweepy
import os

def initialize():
    global api, auth, user
    # Enter your own keys here
    consumer_key = "wXXXXXXXXXXXXXXXXXXXXXXX1"
    consumer_secret = "qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXh"
    access_token = "9XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi"
    access_token_secret = "kXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXT"

    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    user = api.me()


def getStatus():
    lines = []
    while True:
        line = raw_input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status


def tweetthis(type):
    if type == "text":
        print "Enter your tweet "+user.name
        tweet = getStatus()
        try:
            api.update_status(tweet)
        except Exception as e:
            print e
            return
    elif type == "pic":
        print "Enter pic path "+user.name
        pic = os.path.abspath(raw_input())
        print "Enter status "+user.name
        title = getStatus()
        try:
            api.update_with_media(pic, status=title)
        except Exception as e:
            print e
            return

    print "\n\nDONE!!"


def main():
    doit = int(raw_input("\n1. text\n2. picture\n"))
    initialize()
    if doit == 1:
        tweetthis("text")
    elif doit == 2:
        tweetthis("pic")
    else:
        print "OK, Let's try again!"
        main()


main()
