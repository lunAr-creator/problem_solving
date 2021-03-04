'''
Write a program that prints the numbers from 1 to 100. But for multiples of three print 
“Fizz” instead of the number and for the multiples of five print “Buzz” and for the multiples
of both 5 and 3 print 'FizzBuzz'
'''

# My Solution:

for i in range(1,101):
	if i % 5 == 0 and i % 3 == 0:
		print('Fizzbuzz')
	elif i % 5 == 0:
		print('buzz')
	elif i % 3 == 0:
		print('Fizz')
	else:
		print(i)