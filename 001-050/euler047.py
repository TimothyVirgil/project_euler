'''Solution to Project Euler Problem 47
Code by Timothy Virgil Payne Jr.
Started: 1/25/22
Completed: 2/3/22
'''

'''
1. Generate Prime factorization dictionary
2. Iterate through numbers, if dictionary has exactly 5 keys (original with 4 factors), enumerate counter
3. When we hit 4, return the number.'''


from primecheck import primecheck

def prime_factorization(num):
    pf_dict = {'number': num}

    #if prime... done
    if primecheck(num):
        return pf_dict    
    
    else:
    #case: even num
        if num % 2 == 0:
            num = num // 2
            pf_dict[2] = 1

            while num % 2 == 0:
                pf_dict[2] += 1
                num = num // 2

    #case: odd composite num    
        else:
            for a in range(3, int(num**(0.5)) + 2, 2):
                if num % a == 0:                    
                    pf_dict[a] = 1
                    num = num // a
                    break

        if num == 1:
            return pf_dict

        #number must be odd at this point
        while not (primecheck(num) or num == 1):            
            for a in range(3, int(num**0.5)+2, 2):                
                if num % a == 0:
                    try:
                        #if factor exists iterate its exponent
                        pf_dict[a] += 1
                        num = num // a
                    
                    except:
                        #initial factor
                        pf_dict[a] = 1
                        num = num // a
        
        else:
            if num == 1:
                return pf_dict
            else:
                try:
                    #if factor exists
                    pf_dict[num] += 1
                    return pf_dict
                except:
                    #initial facotr
                    pf_dict[num] = 1
                    return pf_dict

pf_count = 0
num_list = []
check_num = 4

while pf_count < 4:
    curr_fact = prime_factorization(check_num)
    if len(curr_fact) == 5:
        pf_count += 1
        num_list.append(check_num)
        check_num += 1
    else:
        pf_count = 0
        num_list = []
        check_num += 1

print(num_list[0])
