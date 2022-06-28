'''Solution to Project Euler Problem 27
Code by Timothy Virgil Payne Jr.
Started: 5/13/2020
Completed: 1/24/2021
b has to be a prime less than 1000.
a can be a positive or negative less than 1000. It seems like it will be a
negative but I am not sure.

Edit 11/28/2020: I'm pretty sure I read this whole damn thing wrong.

I was trying to find the maximum number of primes and not the maximum consecutive?

I'll try this again.

'''
from Euler007 import primecheck # does what is says
import time
start_time = time.time()

def quad_form(n):

    global a
    global b

    output = n**2 + a*n + b

    return output

#need to check for a +- 1 - 1000 and b +- 1 - 1000

# if i do all of them that's 2000 * 2000 which is 4,000,000 checks. Not so many for brute force.

#cycle through all values
#check for consecutive primes
#store the a and b for the most consecutive
#at the end of the day, return a*b

max_prime_tup = (0,0,0)

for a in range(-999,999):

    for b in range(-1000,1001):

        n = 0

        while primecheck(quad_form(n)):

            n += 1

        else:

            if n > max_prime_tup[0]:

                max_prime_tup = (n,a,b)

print(f'n^2 + {max_prime_tup[1]}n + {max_prime_tup[2]} produces {max_prime_tup[0]} consecutive primes.')
print(max_prime_tup[1]*max_prime_tup[2])

                    
print('Total time: {}'.format(time.time()-start_time))                  
        
                        
                        
                    
                    
                    
                    
                    
                    
                
                
                
                
            
        







