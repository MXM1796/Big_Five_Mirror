import pymongo
from pymongo.mongo_client import MongoClient
import urllib
from urllib import parse

def get_database():

   password = urllib.parse.quote_plus('8uq2xcHPjybNd8df')
   user = urllib.parse.quote_plus('testuser')

   uri = f"mongodb+srv://{user}:{password}@clusterbf.ws0mt7y.mongodb.net/?retryWrites=true&w=majority"
   # Create a new client and connect to the server
   client = MongoClient(uri)

   # Create the database for our example (we will use the same database throughout the tutorial
   return client['BigFive']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
   # Get the database
   dbname = get_database()