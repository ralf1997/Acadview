#Q1
import pymongo
client = pymongo.MongoClient()
data = client['Students1']
collection = data['Stud']

#Q2 #Q3
'''for i in range(10):
    name = input('Enter name')
    marks = int(input('Enter marks'))
    collection.insert_one({'Name':name,'Marks':marks})'''
d = collection.find()
for doc in d:
    print(doc)

#Q4
print("Marks greater than 80 are:")
p=collection.find({'Marks':{'$gt':80}})
for i in p:
    print(i)
