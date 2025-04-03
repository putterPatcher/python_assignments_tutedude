a = int(input("Enter a whole number: "))
	
if a < 0:
	print("Enter a whole number")
elif a == 0:
	print(1)
else:
	def factorial(a):
		if a == 1:
			return 1
		else:
			return factorial(a-1)*a
	print("Factorial of {} is {}".format(a, factorial(a)))

