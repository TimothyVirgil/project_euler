# Solution to Project Euler Problem 16
# Code by Timothy Virgil Payne Jr.
# Started: 10/07/19 7:45 PM
# Completed: 10/10/19 4:49 PM

#Let's make a dictionary of numbers to word length

import sys

num_length = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7,
			17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7,}


lett_count = len('onethousand')

for x in range(1,1000):

	a = x // 100 #hundreds digit

	b = x - (a * 100) #ten and one digits

	c = (b // 10) #tens digit

	d = b - (c * 10) # ones digit

	e = c * 10 # tens quantity

	if x >= 100:
		
		if x % 100 == 0:			

			lett_count += (num_length[a] + num_length[100])

			continue

		else:

			lett_count += (num_length[a] + num_length[100] + 3) # the three is the and
			
			if ((b > 10 and b < 20) or ((b % 10) == 0)):

				lett_count += num_length[b]

				continue

			else:				

				if c != 0:

					lett_count += (num_length[d] + num_length[e])

				else:

					lett_count += num_length[d]

	else:

		if ((b > 10 and b < 20) or ((b % 10) == 0)):

				lett_count += num_length[b]

				continue

		else:				

			if c != 0:

				lett_count += (num_length[d] + num_length[e])

			else:

				lett_count += num_length[d]


print(f'The letter count of the first 1000 numbers is {lett_count}.')

wait = input("Press enter to exit.")

sys.exit()





