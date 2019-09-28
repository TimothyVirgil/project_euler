# Solution to Project Euler Problem 11
# Code by Timothy Virgil Payne Jr.
# Started: 09/27/19 1:41 PM
# Completed: 09/28/19 6:29 PM

#We are working with a 20x20 matrix
#There are four different combos:
#1. Right to left - 20 rows
#2. Up to down - 20 columns
#3. Negatively sloped diagonal lines - 33 total lines of various lengths
#4. Positively sloped diagonal lines - 33 total lines of various lengths

#For the rows, we can loop through each row up to the 20th entry
#Same for columns
#For the diagonals It could be best to treat it as two sets
#where one set goes down one side of the matrix
#and the other goes down the other side
#So this would split the diagonals into
#one set of 17 and one set of 16
import sys

from Euler011a import twenty_matrix # Store the data in a separate file
from Euler008 import prod #import our product function


def prod_check():

	global curr_prod
	global max_prod

	if curr_prod > max_prod:

		max_prod = curr_prod

curr_prod = 0
max_prod = 0

#rows

for a in range(0, 400, 20): #Adding four

	for b in range(17):

		curr_prod = prod(twenty_matrix[ (a+b) : (a + b + 4) ])

		prod_check()



#Cols:

for a in range(20):

	for b in range(a, a + 340, 20):

		curr_prod = prod([twenty_matrix[b+(20*x)] for x in range(4)])

		prod_check()



#Neg slope diagonals - top row

for a in range(17,0,-1):

	for b in range((17-a), (17 + 20 * a), 21):

		curr_prod = prod([twenty_matrix[b + (21 * x)] for x in range(4)])

		prod_check()

		

#Neg slope diagonals - starting from left most column

for a in range(16, 0, -1):

	for b in range( (17 - a) * 20, 320 + a, 21):

		curr_prod = prod([twenty_matrix[b + (21 * x)] for x in range(4)])

		prod_check()

#Pos slope diagonals - top row left to right

for a in range(17):

	for b in range(a + 3, (19 * a + 22), 19):

		curr_prod = prod([twenty_matrix[b + (19 * x)] for x in range(4)])

		prod_check()

#pos slope diagonals right most column up to down

for a in range(16, 0, -1):

	for b in range( (359 - 20 * (a)), 359 - a, 19 ):

		curr_prod = prod([twenty_matrix[b + (19 * x)] for x in range(4)])

		prod_check()

print(f'The maximum product of four adjacent numbers is {max_prod}.')

wait = input('Press enter to continue.')

sys.exit()










