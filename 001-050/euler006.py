# Solution to Project Euler Problem 6
# Code by Timothy Virgil Payne Jr.
# Completed: 05/16/19

sum_of_squares = 0

natural_sum = 0

for x in range(1,101):

    sum_of_squares += x ** 2

    natural_sum += x

square_of_sum = natural_sum ** 2



print(square_of_sum - sum_of_squares)

    




    
