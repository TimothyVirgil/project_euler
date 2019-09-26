# Solution to Project Euler Problem 8
# Code by Timothy Virgil Payne Jr.
# Started: 09/26/19 4:03 PM
# Completed: 09/26/19 4:49 PM

#We need to find th 13 digit with the highest average
#We can slice through the number as a string and store the running highest total
#At the end we can find the product

max_product = 0

def prod(a): #product function

	run_prod = 1

	for x in a:

		run_prod *= x

	return(run_prod)


from Euler008a import thousand_digit # import the number from a separate file to help w/ clutter

for a in range(len(thousand_digit)-13):

	thirteen_adjacent = list(thousand_digit[a:a+13]) #slice 13 numbers

	thirteen_adjacent = list(map(int, thirteen_adjacent)) #list of integers

	curr_product = prod(thirteen_adjacent) #multiply together

	if curr_product > max_product:

		max_product = curr_product


print(f'The maximum product is {max_product}')

wait = input('Press a button to exit')







	



