# Solution to Project Euler Problem 2
# Code by Tim Payne
# Completed: 03/14/2019

a = 1
b = 2
solution = 2

while b <= 4_000_000:
    a , b = b , a + b
    
    if b % 2 == 0:
        solution += b

print(solution)

    
