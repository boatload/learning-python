#Write a program that prints the numbers 1 to 1000
#But for multiles of three print "Fizz" instead of the number
#And for multiples of five print "Buzz" instead of the number
#For multiples of both, print "Fizzbuzz"

#Hint: % modulo tells you what's left over when you divide one number by another
#Example: number % 3 = 0

for number in range(1,1001):
	if number % 15 == 0:
		print("FizzBuzz")

	elif number % 3 == 0:
		print("Fizz")

	elif number % 5 == 0:
		print("Buzz")

	else: print(number)