#Q1

import sqlite3
com = sqlite3.connect('Students.db')
print("Created")
com.close()

#Q2 #Q3

try:
    com = sqlite3.connect('Students.db')
    cursor = com.cursor()
   
    for i in range(10):
        print("Enter name " , i , " and marks " , i)
        n = input()
        m = int(input())
        query = 'insert into stud(name,marks) values(?,?)'
        cursor.execute(query,(n,m))
    com.commit()
except sqlite3.DatabaseError as e:
    if com:
        com.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if com:
        com.close()

#Q4
        
try:
    com = sqlite3.connect('Students.db')
    cus = con.cursor()
    query = 'Select * from stud where marks>80'
    cus.execute(query)
    data = cus.fetchall()
    for row in data:
        print('Name: {} , Marks: {}'.format(row[0], row[1]))
except sqlite3.DatabaseError as e:
    if com:
        com.rollback()
        print('Problem occured: ', e)
    
finally:
    if cus:
        cus.close()
    if com:
        com.close()
