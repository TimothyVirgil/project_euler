'''Solution to Project Euler Problem 27
Code by Timothy Virgil Payne Jr.
Started: 5/13/2020
Completed:
b has to be a prime less than 1000.
a can be a positive or negative less than 1000. It seems like it will be a
negative but I am not sure.

Edit 11/28/2020: I'm pretty sure I read this whole damn thing wrong.

I was trying to find the maximum number of primes and not the maximum consecutive?

I'll try this again.

'''
from Euler007 import primecheck
import time
start_time = time.time()

max_length = 1
a_b_prod = 0

for b in range(3,1000,2):    
    
    if primecheck(b):        
                
        for a in range(1,1000,2):
            
            curr_pos_length = 1
            
            for n in range(1,a):              
                                
                if primecheck(n**2 + a*n + b):
                    
                    curr_pos_length += 1                
                                   
                else:
                    
                    if curr_pos_length > max_length:
                        
                        max_length = curr_pos_length
                        
                        a_b_prod = (a * b, a, b, max_length, curr_pos_length)
                        
                    break
                    
        for a in range(1,1000,2):
            
            curr_neg_length = 1
            
            for n in range(1,a):              
                                
                if primecheck(n**2 - a*n + b):
                    
                    curr_neg_length += 1                
                                   
                else:
                    
                    if curr_neg_length > max_length:
                        
                        max_length = curr_neg_length
                        
                        a_b_prod = (-a * b, -a, b, max_length, curr_neg_length)
                        
                    break
                    
print(a_b_prod)
                    
print('Total time: {}'.format(time.time()-start_time))                  
        
                        
                        
                    
                    
                    
                    
                    
                    
                
                
                
                
            
        







