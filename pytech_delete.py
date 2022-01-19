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

matt = {
    "first_name":"Matt", "last_name":"Hunt", "student_id":1010
}

matt_student_id = students.insert_one(matt).inserted_id
print("\n -- INSERT STATEMENTS --")
print("Inserted student record Matt Hunt into the students collection with document id ", matt_student_id)

print("\n -- DISPLAYING STUDENT TEST DOC --")

matt = {
    "first_name":"Matt", 
    "last_name":"Hunt", 
    "student_id":1010
}

print(matt)

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
