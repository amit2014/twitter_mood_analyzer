#!/usr/bin/python

# Coding project for Mevoked
# Kaylee Moser
# Python version 2.7.10

# libraries
import sys
import tweepy
import string
import matplotlib.pyplot as plt
from openpyxl import load_workbook


def get_mood(tweet):
    # Open spreadsheet of values
    wb = load_workbook('bag_of_words.xlsx')
    ws = wb.active
    
    #create variables for positive words and negative words
    pos = 0
    neg = 0
    
    # for each word in tweet, search spreadsheet for matching word
    # if word matches, get negative/positive value and add to variable
    for word in tweet:
        for row in ws.iter_rows('A1:B230'):
            word = word.strip('#,@')
            if (word.lower() == row[0].value):
                if (row[1].value == 'negative'):
                    neg += 1
                else:
                    pos +=1
                break
    
    # find mood number by taking total number of positive words and subtracting total
    # number of negative words
    mood_number = pos - neg
    return mood_number

def plot_mood(dates,moods):
    plt.plot(dates,moods)
    plt.ylabel('Mood Level')
    plt.show()


def main():
    # consumer keys and access tokens, used for OAuth
    consumer_key = 'ArJTlGOeA7rnIHyiPZkHmMhIJ'
    consumer_secret = 'zr7Ldopc0QdwxvsMwBcFFYk3LsWUPeuKEkfo6wj9848W4x7eq0'
    access_token = '1550061679-WpJunbZbtwCGXL84wQbyzmOuSre1tNh7iloJyQV'
    access_token_secret = 'PusPCv8NgalPKSagKNMioU8xpP77TrhSXS9wKH0A5K8bE'
    
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # Creation of actual interface, using authentication
    api = tweepy.API(auth)

    # Get Twitter user name from program user
    screen_name = raw_input("Please enter the Twitter handle: ")

    # Gather recent tweets, split each tweet into a list of words
    recent_tweets = api.user_timeline(screen_name)
    moods = []
    dates = []
    for tweet in recent_tweets:
        moods.append(get_mood(tweet.text.split()))
        dates.append(tweet.created_at)

    plot_mood(dates,moods)


if (__name__ == '__main__'):
    main()


