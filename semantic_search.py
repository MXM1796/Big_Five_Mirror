from txtai.embeddings import Embeddings
import pandas as pd
import numpy as np
import plotly.express as px

import json

embeddings = Embeddings({
    'path': "sentence-transformers/all-MiniLM-L6-v2"
})

embeddings.load("test2_index1")

test_csv = pd.read_csv("test2.csv", header=0, index_col=False, usecols=[1])
test_csv.reset_index()

data = test_csv["text"]

txtai_data = []

for count, sent in enumerate(data):
    txtai_data.append((count, sent, None))

# embeddings.index(txtai_data)

word_arr_openess = ["travel", "exploring", "world", "new", "open", "experience", "curious"]
word_arr_concs = ["organized", "carefully", "planed", "effective", "responsible", "reliable", "deliberate"]
word_arr_extrv = ["sociable", "activ", "chatty", "warmly", "optimistic", "serene","Enthusiastic"]
word_arr_agrgb = ["Altruism", "Understanding", "Goodwill", "Compassion", "Cooperativeness","Resilience", "emphatic"]
word_arr_nrcm = ["fear","Nervousness","tension", "Mourning", "Uncertainty","Embarrassment", "Worries"]

words_arr = [word_arr_openess,word_arr_concs,word_arr_extrv,word_arr_agrgb,word_arr_nrcm]

def score_calc(score_arr):
    """
    test test test
    """
    avg_sum_arr = []
    for val in score_arr.values():
        if len(val) != 0:
            avg_val = np.average(val)
            avg_sum_arr.append(avg_val)
    avg_score = np.average(avg_sum_arr)

    return avg_score

def score_coll(word_arr,score=0.5):
    score_dict = {}
    for word in word_arr:
        res = embeddings.search(word, 10)
        score_arr = []
        for item in res:
            if item[1] > score:
                score_arr.append(round(item[1],2))

        score_dict[word] = score_arr

    return score_calc(score_dict)

score_arr_full = [round(score_coll(arr, 0.4),2) for arr in words_arr]

