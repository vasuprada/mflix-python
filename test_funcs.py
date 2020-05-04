from pymongo import MongoClient

uri = "mongodb+srv://m220student:m220password@sandbox-qdud1.mongodb.net/test"
mc = MongoClient(uri)

print(mc.stats)