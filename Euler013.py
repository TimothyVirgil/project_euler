# Solution to Project Euler Problem 13
# Code by Timothy Virgil Payne Jr.
# Started: 10/01/19 7:45 PM
# Completed: 10/01/19 8:02 PM

#We will import the list of numbers from Euler013a.py
#In that file, we copied the text, took out the new lines
#and converted to a list of integers
#All we have to do here is find the sum.

from Euler013a import num_list
import sys

fifty_sum = sum(num_list)

print(f'The first ten digits of the sum are: {str(fifty_sum)[0:10]}.')

wait = input('Press enter to exit.')

sys.exit()