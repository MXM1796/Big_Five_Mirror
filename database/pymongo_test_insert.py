# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
import datetime

# get data from BigFive Database
# bf_db = get_database()
# collection_name = bf_db["scores"]

# creating current date
today = datetime.datetime.now()
time = today.strftime("%X")
date = today.strftime("%x")


# Upload (to MongoDB) function
def item_generator(youtube_url):
  #create item
  item = {
    "item_name": f"youtube_url",
    "youtube Url": youtube_url,
    "date": date,
    "time": time
  }

  return item


def upload_function(youtube_url):
  item = item_generator(youtube_url)
  # select database BigFive Database and collection name
  bf_db = get_database()
  collection_name = bf_db["scores"]

  collection_name.insert_many([item])

  return "successfull upload"


