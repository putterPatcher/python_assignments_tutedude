try:
	with open('sample.txt', "r") as file:
		print("Reading file content:")
		for i in enumerate(file.readlines()):
			print("Line {}: {}".format(i[0]+1, i[1][:-2]))
except:
	print("Error: The file 'sample.txt' was not found.")

