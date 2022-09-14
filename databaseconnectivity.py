from pymongo import MongoClient
#create an instance
client=MongoClient("mongodb://127.0.0.1:27017")
#create db
db=client['s3']
#create collection
studentdetails=db.students
#create Document
student1={"regd":"111","name":"abc"}
student2=[{"regd":"222","name":"abc"},{"regd":"333","name":"def"},{"regd":"444","name":"ghi"}]
studentdetails.insert_one(student1)
studentdetails.insert_many(student2)

#insert single


#Ret Document
#ret  single Document
print(studentdetails.find_one())

#Ret multiple documents
a={"name":"abc"}
for x in studentdetails.find(a):
    print(x)

#delete documents
#delete single document
b={"regd":"222"}
studentdetails.delete_one(b)

c={"name":"abc"}
studentdetails.delete_many(c)

#