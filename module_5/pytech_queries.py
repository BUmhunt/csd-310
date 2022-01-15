import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client["pytech"]
students = db["pytech"]

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = db.Students.find({})

thorin = {
    "first_name":"Thorin", 
    "last_name":"Oakenshield", 
    "student_id":1007
}
print(thorin)

bilbo = {
    "first_name":"Bilbo", 
    "last_name":"Baggins", 
    "student_id":1008
}

print(bilbo)

frodo = {
    "first_name":"Frodo", 
    "last_name":"Baggins", 
    "student_id":1009
}
print(frodo)
print("\n -- DISPLAYING STUDENTS DOCUMENT FROM find_one() QUERY --")


thorin2 = {
    "first_name":"Thorin", 
    "last_name":"Oakenshield", 
    "student_id":1007
}

doc = db.Students.find_one({"student_id":"1007"})
print(thorin2)

