from pymongo import MongoClient
MONGO_URI = "mongodb+srv://<user>:<password>@cluster0.afakb9j.mongodb.net/notes"

conn = MongoClient(MONGO_URI)