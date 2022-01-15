import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:<password>@cluster0.vayt5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient('localhost', 27017)

db = client.pytech

print("\n --Pytech Collection List --")
print(db.list_collection_names())
input("\nEnd of program, press any key to exit...\n")
