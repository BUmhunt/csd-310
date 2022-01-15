MongoDB: insert_one()
fred = {
    "first_name":"Fred"
}

fred_student_id = students.insert_one(fred).inserted_id

print(fred_student_id)

MongoDB: find()
docs = db.collection_name.find({})
print(doc)

MongoDB: find_one() 
doc = db.collection_name.find_one({"student_id":"1007"})

print(doc["student_id"])

