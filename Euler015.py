# Solution to Project Euler Problem 15
# Code by Timothy Virgil Payne Jr.
# Started: 10/02/19 5:16 PM
# Completed: 10/07/19 12:52 PM

#This is a combinatorics problem
#For any grid, the total amount of moves will be the sides of the grid times two
#So, for a 3x3 there will be 6 moves, a 2x2, 4 moves, a 4x4 8 moves, and so on.
#For a 20x20, there will be 40 moves.
#Each option, down or right will appear 20 times.
#We can find the total possible amount of moves divided by the repeated elements.
#So, We have 40 total move combinations divided by 20 move combinations times 20 move combinations

from math import factorial
import sys

ans = factorial(40) // (factorial(20) * factorial(20))

print(f'The number of ways to move through the 20 x 20 grid is {ans}.')

wait = input("Press enter to exit.")

sys.exit()

