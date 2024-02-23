# Import required modules and libraries
import pathlib
from txtai.embeddings import Embeddings
import pandas as pd
import numpy as np
import os

# Initialize txtai Embeddings with a pre-configured model
embeddings = Embeddings({
    'path': "sentence-transformers/all-MiniLM-L6-v2"
})

# Load test data from a CSV file
test_csv = pd.read_csv('../test2.csv', header=0, index_col=False, usecols=[1])

# Reset the DataFrame index
test_csv.reset_index(inplace=True)

# Extract the 'text' column from the DataFrame
data = test_csv["text"]

# Prepare data for txtai indexing
txtai_data = [(count, sent, None) for count, sent in enumerate(data)]

# Index data with txtai
embeddings.index(txtai_data)

# Define word lists for different personality traits
word_arr_openess = ["travel", "exploring", "world", "new", "open", "experience", "curious"]
word_arr_concs = ["organized", "carefully", "planed", "effective", "responsible", "reliable", "deliberate"]
word_arr_extrv = ["sociable", "activ", "chatty", "warmly", "optimistic", "serene", "Enthusiastic"]
word_arr_agrgb = ["Altruism", "Understanding", "Goodwill", "Compassion", "Cooperativeness", "Resilience", "emphatic"]
word_arr_nrcm = ["fear", "Nervousness", "tension", "Mourning", "Uncertainty", "Embarrassment", "Worries"]

# Combine word lists into one list
words_arr = [word_arr_openess, word_arr_concs, word_arr_extrv, word_arr_agrgb, word_arr_nrcm]

def score_calc(score_arr):
    """
    Calculate the average of the scores.

    Parameters:
    - score_arr: Dictionary containing scores for each word.

    Returns:
    Average score.
    """
    avg_sum_arr = []
    for val in score_arr.values():
        if len(val) != 0:
            avg_val = np.average(val)
            avg_sum_arr.append(avg_val)
    avg_score = np.average(avg_sum_arr)

    return avg_score

def score_coll(word_arr, score=0.5):
    """
    Calculate the score for a word list.

    Parameters:
    - word_arr: List of words.
    - score: Threshold score.

    Returns:
    Score for the word list.
    """
    score_dict = {}
    for word in word_arr:
        res = embeddings.search(word, 10)
        score_arr = []
        for item in res:
            if item[1] > score:
                score_arr.append(round(item[1], 2))

        score_dict[word] = score_arr

    return score_calc(score_dict)

# Calculate the score for all personality traits
score_arr_full = [round(score_coll(arr, 0.4), 2) for arr in words_arr]

print(score_arr_full)
