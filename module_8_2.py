from peewee import *

conn=SqliteDatabase('module_8_1.sqlite')

class Students(Model):
	id = IntegerField(column_name='id', primary_key=True)
	name = CharField(column_name='name')
	surname = CharField(column_name='surname')
	age = IntegerField(column_name='age')
	city = CharField(column_name='city')

	class Meta:
		database=conn


class Courses(Model):
	id = IntegerField(column_name='id', primary_key=True)
	name = CharField(column_name='name')
	time_start = CharField(column_name='time_start')
	time_end = CharField(column_name='time_end')

	class Meta:
		database=conn


class Student_courser(Model):
	student_id = ForeignKeyField(Students)
	course_id = ForeignKeyField(Courses)

	class Meta:
		database=conn

#Students.create_table()
#Student_courser.create_table()
#Courses.create_table()


student = Students(name="Max", surname="Brooks", age=24, city="Spb")
student.save()
student = Students(name="John", surname="Stones", age=15, city="Spb")
student.save()
student = Students(name="Andy", surname="Wings", age=45, city="Manchester")
student.save()
student = Students(name="Kate", surname="Brooks", age=34, city="Spb")
student.save()

courses = Courses(name="python", time_start="21.07.2021", time_end="21.08.2021")
courses.save()
courses = Courses(name="java", time_start="13.07.2021", time_end="16.08.2021")
courses.save()

student_course = Student_courser(student_id=1, course_id=1)
student_course.save()
student_course = Student_courser(student_id=2, course_id=1)
student_course.save()
student_course = Student_courser(student_id=3, course_id=1)
student_course.save()
student_course = Student_courser(student_id=4, course_id=2)
student_course.save()




#student_30 = Students.select().where(Students.age > 30)
#for i in student_30:
#    	print(i.name)
#print('\n')

#students_python = Students.select().join(Student_courser).where(Student_courser.course_id == 1)
#for r in students_python:
#	print(r.name, r.surname)
#print('\n')

#students_spb = Students.select().join(Student_courser).where(
#    Student_courser.course_id == 1, Students.city == 'Spb')
#for k in students_spb:
#    print(k.name, k.surname)
#print('\n')