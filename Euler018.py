# Solution to Project Euler Problem 18
# Code by Timothy Virgil Payne Jr.
# Started: 10/11/19 3:00 PM
# Completed: 10/12/19 1:18 PM

import sys

from Euler018a import row_list

# we can go row by row to eliminate the amount of paths we have to test
# This is a classic algorithm problem (I think)
# We will only keep the largest possible quantities in each row to greatly limit
# the iteration required to solve the problem.

prev_list = [row_list[0][0] + row_list[1][0], 
			 row_list[0][0] + row_list[1][1]] # This is the sum up to row 2

for a in range(2, len(row_list)):  ## iterate through our list of triangle rows

    curr_list = [] ## our current list of totals

    curr_list += [ row_list[a][0] + prev_list[0] ] ## add the left most values to current total list

    for b in range(1, len(prev_list)): ## iterate through current row of triangle, finding the current max

        curr_list += [ max(prev_list[b-1], prev_list[b]) + row_list[a][b] ]

    curr_list += [ row_list[a][-1]  + prev_list[-1] ] ## add the right most values

    
    prev_list = curr_list ## refresh current list    

print(f'The maximum sum is {max(curr_list)}.') ## find the highest total

wait = input("Press enter to exit.")

sys.exit()