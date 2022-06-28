'''This module holds the primecheck function
which is commonly used in these Euler solutions.'''

def primecheck(a:num) -> bool:
    
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