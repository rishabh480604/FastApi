from pymongo import MongoClient
import certifi
# DB is configured with notes have notes folder
MONGO_URI = "mongodb+srv://rishabh22356:asdfghjkl@cluster0.ymgsy.mongodb.net"

conn=MongoClient(MONGO_URI,
                  tls=True,
                  tlsCAFile=certifi.where())


