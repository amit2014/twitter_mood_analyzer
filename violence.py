#!/usr/bin/python

# Coding project for Mevoked
# Kaylee Moser
# Python version 2.7.10

# libraries
import sys
from openpyxl import load_workbook

def violence_features(tweet):
    features = {}
    # open bag of violent words
    wb = load_workbook('violent_bag.xlsx')
    ws = wb.active

    # check to see if any violent words in tweet, return list
    violent_words = []
    at_mentions = []
    for word in tweet:
        # if word is a mention, skip
        if (word[0] == '@'):
           at_mentions.append(word) 
        else:
            # remove hashtags and punctuation, change to lower-case
            word = word.lower().strip(' ,#,,,.,!,?')
            for row in ws.iter_rows('A2:B495'):
                if (word == row[0].value):
                    violent_words.append(word)
                    break
    features['violent_words'] = violent_words
    features['violent_freq'] = len(violent_words)
    features['at_mentions'] = at_mentions
    #features["violent_freq"] = len(violent_words)
    #features["at_mentions"] = get_tagged_users(tweet)
    #features["tense"] = get_tense(tweet)
    #features["category"] = get_category(tweet,ws)
    return features

#def get_violent_words(tweet):
#
#
#def get_tagged_users(tweet):
#
#
#def get_tense(tweet):
#
#
#def get_category(tweet):


def main():
    tweet = sys.stdin.readline().split()
    features = violence_features(tweet)
    for key in features:
        print "{} : {}".format(key,features[key])


if (__name__ == '__main__'):
    main()
