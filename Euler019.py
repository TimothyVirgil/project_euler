'''Solution to Project Euler Problem 19
Code by Timothy Virgil Payne Jr.
Started: 10/12/19 1:45 PM
Completed: 10/15/19 3:59 PM

I use the date objects in the datetime module to
cycle through all the days and check the day of the month and day of the week.
This algorithm could be faster, but since it is only thousands of objects and computers
are fast, it's plenty efficient for us!'''

#Find how many Sundays were on the first of the month
#from 1901-2000
#

import sys

from datetime import date

first_day = date(1901, 1, 1).toordinal() #Date as integer
last_day = date(2000, 12, 31).toordinal() #last day as integer

first_sun_count = 0

for a in range(first_day, last_day + 1):

	curr_day = date.fromordinal(a)

	if curr_day.day == 1 and curr_day.weekday() == 6:

		first_sun_count += 1

	else:

		continue

else:

	print(f'The number of Sundays that occured on the first of the month is {first_sun_count}.\n')

	wait = input("Press enter to exit.")

	sys.exit()

