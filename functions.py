import re
from nltk import sent_tokenize
from nltk import word_tokenize
from datetime import datetime


def sort_strings_by_date(strings):
    def extract_date(string):
        date_str = string.split('(')[-1].split(')')[0].strip()
        return datetime.strptime(date_str, '%B %d, %Y')

    # Sort strings based on extracted dates
    return sorted(strings, key=extract_date)

# finds the date in a string
def find_date(text_with_date):

    date_pattern = r"(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b)"

    match = re.search(date_pattern, text_with_date)

    if match:
        date_string = match.group(0)

        date_obj = datetime.strptime(date_string, "%B %d, %Y")

        formatted_date = date_obj.strftime("%B %d, %Y")

        return formatted_date
    else:
        return "Date not found in the input string."


# reformat the date to the form of xx/xx/xxxx
def reformat_date(date_str):
    date_obj = datetime.strptime(date_str, "%B %d, %Y")

    formatted_date = date_obj.strftime("%m/%d/%Y")

    return formatted_date

# remove the date from the string
def remove_date(string):
    # Define the regular expression pattern to match the date at the end of the string
    pattern = r'\s*\((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th),\s+\d{4}\)\s*$'
    # Replace the matched pattern with an empty string
    result = re.sub(pattern, '', string)
    return result.strip()  # Trim any leading or trailing whitespace


def remove_extra_spaces(input_string):
    # Remove leading and trailing spaces
    input_string = input_string.strip()

    # Replace multiple spaces with a single space
    input_string = re.sub(r'\s+', ' ', input_string)

    # Remove spaces after punctuation marks except for $, and remove spaces after $
    input_string = re.sub(r'\s+([.,!?])(?=[^$])|(?<=\$)\s+|\s+([.,!?])(?=$)', r'\1\2', input_string)

    return input_string


# filters the tweets in a list
def makeFilteredList(tweets, stopword_filter, lemmatizer):

    tweets = [remove_date(string) for string in tweets]

    # create a 2D array of tweets split into sentences
    for tweet in tweets:
        tweet_sent = [sent_tokenize(tweet) for tweet in tweets]

    tweet_words = []

    for tweet in tweet_sent:
        tweet_words.append([word_tokenize(sentence) for sentence in tweet])

    filtered_tweet_words = []

    for tweet in tweet_words:
        filtered_tweet = []
        for sentence in tweet:
            sentence_filtered = list(filter(stopword_filter, sentence))
            filtered_tweet.append(sentence_filtered)
        filtered_tweet_words.append(filtered_tweet)

    lemmatized_tweet_words = []

    for tweet in filtered_tweet_words:
        tweet_lemmatized = []
        for sentence in tweet:
            sentence_lemmatized = [lemmatizer.lemmatize(w) for w in sentence]
            tweet_lemmatized.append(sentence_lemmatized)
        lemmatized_tweet_words.append(tweet_lemmatized)

    final_return = []

    for tweet in lemmatized_tweet_words:
        currTweet = ""
        for sentence in tweet:
            currSentence = ""
            for word in sentence:
                currSentence = currSentence + " " + word
            currTweet = currTweet + " " + currSentence
        final_return.append(currTweet)

    actual_final_return = []

    for tweet in final_return:
        actual_final_return.append(remove_extra_spaces(tweet))

    return actual_final_return
