n = int(input("Enter the number of students: "))
a = {}

for i in range(n):
	name = input("Enter name {}: ".format(i+1))
	marks = int(input("Enter marks: "))
	a[name] = marks

while True:
	name = input("Enter the student name: ")
	if name == "":break
	try:
		print("{}'s marks: {}".format(name, a[name]))
	except:
		print("Student not found.")
