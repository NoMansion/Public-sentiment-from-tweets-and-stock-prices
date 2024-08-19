# Analyzing the Relationship Between Public Sentiment From Tweets and Stock Prices #

## Goals: ##
Create a program that would analyze tweets for sentimenet values to make predictions about stock prices. It would also check if general public sentiment is a good indicator of how the market is doing.

## How it works: ##
- Reads data from S&P 500 pandas dataframe.
- Filters tweets to be stored efficiently.
- Analyzes tweets for a sentiment value.
- Plots these values in chronological order from the tweets.
- Plots the S&P 500 values.

## Notes: ##
The original intention with this project was the use the X (formerly Twitter) API to pull tweets from financial accounts. Due to the steep price of accessing X API, I did a workaround by reading tweets from a text file. I hope to one day incorporate the X API!
