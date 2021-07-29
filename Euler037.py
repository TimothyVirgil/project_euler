'''Solution to Project Euler Problem 37
Code by Timothy Virgil Payne Jr.
Started: 7/29/21
Completed: 7/29/21

If there's only eleven primes with this property then
there must be an upper limit.

The final digit must be 3 or 7. the first digit can be 2, 3, 5, or 7. 
For 3 digit and larger, the middle digits must be 3, 7, or 9.

I don't really need to know the upper limit since they told me there's 11. I can break my loop when I hit that number
'''

trunc_sum = 0
trunc_count = 0


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

def trunc_check(a):

	str_prime = str(a)
	global trunc_sum

	for x in range (1, len(str_prime)):
		b = str_prime[:x]
		c = str_prime[-x:]

		if primecheck(int(b)) and primecheck(int(c)):
			continue

		else:
			return False

	else:
		return True


for num in range(11, 1_000_000_000, 2): #I tried to set some number checking conditions but it was slower than just looping
	
	if primecheck(num):

		if trunc_check(num):
			trunc_sum += num
			trunc_count += 1

			if trunc_count == 11:				
				break

			else:
				continue

		else:
			continue

	else:
		continue

print(trunc_sum)





