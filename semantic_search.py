from txtai.embeddings import Embeddings
import json
import pandas as pd
import datetime

# print()
# print(datetime.date())

def date_and_time_func():
    date_time = datetime.datetime.now()
    year = date_time.year
    month = date_time.month
    day = date_time.day
    time = date_time.time()

    return [year, month, day,  time.hour, time.minute]


def filename_generator():
    date_time = datetime.datetime.now()
    year = date_time.year
    month = date_time.month
    day = date_time.day
    time = date_time.time()

    filename = f"dataset_{year}_{month}_{day}_{time.hour}_{time.minute}_{time.second}"
    return filename

print(filename_generator())


path = "test2.csv"

def data_prep(path):
    txtai_data = []

    # read transcript csv
    csv = pd.read_csv(path, header=0, index_col=False, usecols=[1])
    csv = csv["text"].reset_index()

    i = 0
    for index, sentence in csv.iterrows():
        txtai_data.append((i, sentence["text"], None))
        i = i+1
    # for txtai adapted arrary
    return txtai_data


# print(data_prep(path))

def embedding_process(txtai_arr):
    # Initialisierung
    embeddings = Embeddings({
        "path": "sentence-transformers/all-MiniLM-L6-v2"
    })

    embeddings_dict = embeddings.index(txtai_arr)
    embeddings.save(f"Embedded_data/{filename_generator()}")

    return embeddings_dict

openness_keywords = ["new", "explore", "world", "wide", "open", "divers"]

embedding = embedding_process(data_prep(path))

print(embedding)
def openness_score(embeddings_dict):
    similarity_scores_openness = []
    for key in openness_keywords:
        res = embeddings_dict.search(key, 3)
        for item in res:
            # print(item[1])
            similarity_scores_openness.append(item[1])
    return sum(similarity_scores_openness)/len(similarity_scores_openness)

# print(openness_score())
#
# def extraversion_score():
#
# def conscientiousness_score():
#
# def agreeableness_score():
#
# def neuroticism_score():
#
#
#
# # print(similarity_scores_openness)
#
# opennes_score = sum(similarity_scores_openness)/len(similarity_scores_openness)
#
# print(opennes_score)

# res = embeddings.search("hard", 3)
#
# for item in res:
#     print(f"Text: {csv[item[0]]}")
#     print(f"similarity: {item[1]}")
#     print()

# todo semantic search auf alle Eigenschaften anwenden - Blueprint
# todo Funktionen einführen (Objetkorientiert programmieren)
# todo Gewichtung  mit einführen (e-Funktion)