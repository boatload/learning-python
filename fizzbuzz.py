#Write a program that prints the numbers 1 to 1000
#But for multiles of three print "Fizz" instead of the number
#And for multiples of five print "Buzz" instead of the number
#For multiples of both, print "Fizzbuzz"

#Hint: % modulo tells you what's left over when you divide one number by another
#Example: number % 3 = 0

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(1000)
