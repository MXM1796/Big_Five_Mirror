import pymongo
from pymongo.mongo_client import MongoClient
import urllib
from urllib import parse

def get_database():
    """
    Connects to a MongoDB database and returns the specified database.

    Returns:
    pymongo.database.Database: The connected MongoDB database.
    """
    # MongoDB credentials
    password = urllib.parse.quote_plus('8uq2xcHPjybNd8df')
    user = urllib.parse.quote_plus('testuser')

    # MongoDB connection URI
    uri = f"mongodb+srv://{user}:{password}@clusterbf.ws0mt7y.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the MongoDB server
    client = MongoClient(uri)

    # Create or get the specified database ('BigFive' in this case)
    return client['BigFive']

# This block ensures that the code is only executed when the script is run, not when it's imported as a module
if __name__ == "__main__":
    # Get the database and store it in the variable 'dbname'
    dbname = get_database()
