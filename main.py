from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import *


# create a pandas data frame for the S&P 500 prices
usecols = ["Date", "Close/Last"]
sp500_data = pd.read_csv("C:/Users/gsam8/Downloads/HistoricalData_1714358831507.csv", index_col="Date", usecols=usecols)
english_stops = stopwords.words("english")

stopword_filter = lambda word: word.lower() not in english_stops

lemmatizer = WordNetLemmatizer()

# Sorts strings in order by the date at the end of the string

# turns the text file into a list of tweets
file = open("tweets.txt", encoding='utf-8')
content = file.read()
file.close()

# Make list tweet contain every tweet as a string
tweets = content.split('\n')
for tweet in tweets:
    if(tweet.__eq__('')):
        tweets.remove(tweet)

tweets = sort_strings_by_date(tweets)

filtered_tweets = (makeFilteredList(tweets, stopword_filter, lemmatizer))
tweet_sentiments = []
count = 0

# prints orginal tweet, the filtered tweet, and the sentiment value
for tweet in tweets:
    print("Original tweet:")
    print(tweet)
    print("Filtered tweet:")
    print(filtered_tweets[count])
    currentTweet = TextBlob(filtered_tweets[count])
    print("Sentiment value:")
    print(currentTweet.sentiment.polarity)
    tweet_sentiments.append(currentTweet.sentiment.polarity)
    print()
    count = count + 1

dates = []
counter = 0
for tweet in tweets:
    dates.append(find_date(tweet))
    counter = counter + 1

counter = 0

for date in dates:
    dates[counter] = reformat_date(dates[counter])
    counter = counter + 1

sp500_data.plot()
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

avg_sentiment = 0
for value in tweet_sentiments:
    avg_sentiment += value
avg_sentiment = avg_sentiment / len(tweet_sentiments)
print("Average sentiment:")
print(avg_sentiment)
x = np.array(dates)
y = np.array(tweet_sentiments)

plt.title("S&P 500 Prices")
plt.figure()
plt.plot(x, y, color="red")
plt.title("Tweet Sentiment Data")
plt.show()
