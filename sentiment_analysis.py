#############Testing#####################
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression

# Downloading packages for testing and analyzing
# nltk.download(["names", "stopwords", "state_union", "twitter_samples", "movie_reviews", "averaged_perceptron_tagger", "vader_lexicon", "punkt"])

# create word list made up only out of letters
words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
print(nltk.corpus.state_union.words())
# print(words)
# filter out "stopwords" like "and", "I", "a" etc.
stopwords = nltk.corpus.stopwords.words("english")

words = [w for w in words if w.lower() not in stopwords]

# todo schauen, wie ein corpus erstellt wird

fd = nltk.FreqDist(words)

most_common = fd.most_common(3)
table = fd.tabulate(3)

# partial equalization of words
lower_fd = nltk.FreqDist([w.lower() for w in fd])

# Using prebuild sentiment analyzer
sia = SentimentIntensityAnalyzer()


# checks if sentence is negative (-1) or positive (+1)
def polarity(sentence):
    blob = TextBlob(sentence)
    return round(blob.sentiment.polarity, 4)


test_csv = pd.read_csv("test2.csv", header=0, index_col=False, usecols=[1])
test_csv.reset_index()

# Test analysis of youtube script
test_polarity_arr = []
for index, sentence in test_csv.iterrows():
    # print(sentence["text"])
    test_polarity_arr.append(polarity(sentence["text"]))

print(test_polarity_arr)

# Predicting Openess

def predict_openness(posts, scores, words_of_interest):
    # Create a bag-of-words representation of the posts
    vectorizer = CountVectorizer(vocabulary=words_of_interest)
    X = vectorizer.fit_transform(posts)
    X = X.toarray()

    # Fit a linear regression model
    model = LinearRegression().fit(X, scores)

    return model

posts = ['I love to try new things.', 'I am always open to new experiences.', 'I prefer to stick to what I know.']
scores = [5, 4, 2]
words_of_interest = ['new', 'open', 'try', 'experiences']

model = predict_openness(posts, scores, words_of_interest)

# def openness_score():
    #Random guess -  if 20% of the Videotranscript match with list of words representing openness than you have a score of 100.
    #prüfe 1000 worte
    # schau wie viele davon mit den Worten aus der Liste übereinstimmen
    # berechne den Score
    # score = words/200
