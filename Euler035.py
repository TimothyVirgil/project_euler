'''Solution to Project Euler Problem 34
Code by Timothy Virgil Payne Jr.
Started: 7/28/21
Completed:7/28/21'''

prime_count = 13 #The problem said there are 13 under 100

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

def dig_check(a):

    'Cycle the digits, check for primes'

    global prime_count

    str_prime = str(a)

    for c in range(len(str_prime)-1): #cycle for the rest of the primes
        check_str = ''

        for b in range((len(str_prime)-1),-1,-1):
            check_str += str_prime[-b]

        if primecheck(int(check_str)):
            str_prime = check_str
            continue

        else:
            return

    else:
        prime_count += 1

even_digs = ['2','4','6','8','0'] #skipping all evens saves like two seconds

for x in range(101,1_000_000,2):
    even_check = str(x)

    for dig in even_check:
        if dig in even_digs:
            break

    else:
        if primecheck(x):
            dig_check(x)

print(prime_count)


