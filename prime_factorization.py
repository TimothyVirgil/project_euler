from primecheck import primecheck

def prime_factorization(num):

    '''Return a dictionary with the prime factors as keys
    and their exponents as values.'''

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
                    