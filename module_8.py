import sqlite3
from datetime import datetime
con=sqlite3.connect('module_9.sqlite3')
cursor=con.cursor()

#tb_1 = cursor.execute("Create Table Students(id int, name varchar(32), \
                       #surname varchar (32), age int, city varchar (32))")
#tb_2 = cursor.execute("Create Table Courses(id int, name varchar(32), time_start timestamp, \
	                   #time_end timestamp)")

#tb_3 = cursor.execute("Create Table Student_courser(student_id int, course_id int)")

#cursor.execute(tb_1)
#cursor.execute(tb_2)
#cursor.execute(tb_3)

Students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John','Stones', 15, 'Spb'),(3, 'Andy','Wings',  45, 'Manhester'), \
	                                                                         (4, 'Kate', 'Brooks', 34, 'Spb')]

Courses =  [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]

Student_courser = [(1,1), (2,1), (3,1), (4,2)]

cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", Students)
cursor.executemany("INSERT INTO Courses  VALUES (?,?,?,?)", Courses)
cursor.executemany("INSERT INTO Student_courser VALUES (?,?)", Student_courser)


tb1 = cursor.execute("SELECT name, surname FROM Students WHERE age>30")
tb1=cursor.fetchall()
print(tb1)

tb2 = cursor.execute("SELECT * FROM Student_courser JOIN Students ON Student_courser.student_id=Students.id WHERE course_id=1;")
tb2=cursor.fetchall()
print (tb2)

tb3 = cursor.execute("SELECT * FROM Student_courser JOIN Students ON Student_courser.student_id=Students.id WHERE course_id=1 AND city='Spb';")
tb3=cursor.fetchall()
print (tb3)














