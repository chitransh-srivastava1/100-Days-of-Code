#Fizz Buzz in range 1-100
for no in range(1,101):
	if (no%3==0 and no%5==0):
		print("Fizz Buzz")
	elif (no%5==0):
		print("Buzz")
	elif (no%3==0):
		print("Fizz")
	else:
		print(no)
