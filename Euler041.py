'''Solution to Project Euler Problem 41
Code by Timothy Virgil Payne Jr.
Started: 9/7/21
Completed: 9/7/21
'''
from itertools import permutations

def primecheck(a):
    
    'This function checks to see if an integer is prime.' 

    if a == 2 or a == 3:        
        return True

    elif a < 2 or a % 2 == 0:        
        return False

    else:        
        for b in range(3, int(a**(0.5)) + 2, 2):            
            if a % b == 0:                
                return False
            
            else:                
                continue
            
        else:            
            return True

first_num = '123'
max_pan_prime = 0

for a in range(4,10):
    first_num += str(a)

    for b in permutations(first_num):
        test_num =''

        for c in b:
            test_num += c

        if primecheck(int(test_num)):

            if int(test_num) > max_pan_prime:
                max_pan_prime = int(test_num)

            else:
                continue

        else:
            continue

print(max_pan_prime)

            
