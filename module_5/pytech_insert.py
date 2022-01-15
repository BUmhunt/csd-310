import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client["pytech"]
students = db["pytech"]

print("\n -- INSERT STATEMENTS --")

thorin = {
    "first_name":"Thorin", "last_name":"Oakenshield", "student_id":1007
}

thorin_student_id = students.insert_one(thorin).inserted_id

print("Inserted student record Thorin Oakenshield into the students collection with document id ", thorin_student_id)

bilbo = {
    "first_name":"Bilbo", "last_name":"Baggins", "student_id":1008
}

bilbo_student_id = students.insert_one(bilbo).inserted_id

print("Inserted student record Bilbo Baggins into the students collection with document id ", bilbo_student_id)

frodo = {
    "first_name":"Frodo", "last_name":"Baggins", "student_id":1009
}

frodo_student_id = students.insert_one(frodo).inserted_id

print("Inserted student record Frodo Baggins into the students collection with document id ", frodo_student_id)


