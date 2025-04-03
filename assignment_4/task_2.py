with open('output.txt', "w") as file:
	a = input("Enter text to write to the file: ")
	file.write(a+"\n")
	a = input("Enter additional text to append: ")
	file.write(a)
with open('output.txt', 'r') as file:
	print("\nFinal content of output.txt: ")
	print(file.read())

