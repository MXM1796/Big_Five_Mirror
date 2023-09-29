# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
import semantic_search
import datetime

# get data from BigFive Database
bf_db = get_database()
collection_name = bf_db["scores"]

# creating current date
today = datetime.datetime.now()
time = today.strftime("%X")
date = today.strftime("%x")

#create first prototype item

item_1 = {
  "item_name" : "Blender",
  "score_arr": semantic_search.score_arr_full,
  "date": date,
  "time": time
}

collection_name.insert_many([item_1])


