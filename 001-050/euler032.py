'''Solution to Project Euler Problem 32
Code by Timothy Virgil Payne Jr.
Started: 6/24/2021
Completed: 7/8/2021

Our multiplaction statement must have 9 digits.

So this gives us an idea of our constraints.

Working on paper, I've figured out that we must have a statement that looks like:

ab * cde = fghi

where a-i are unique digits from 1-9.

there are a handful that work in the form

a * bcde = fghi.

I could make a separate loop to test these and limit the compute time,
but it should be trivial either way.

either way, the product must be less than ten thousand.
'''
prod_sum = 0
prod_list =[] #to check for dupliucates

for a in range(2,80): #anything higher will push over our product limit of 10,000

    for b in range(124,5000): #anything higher will break limit
        c=a*b

        if c >= 10000:
            break

        else:
            pan_check=str(a)+str(b)+str(c)

        if len(pan_check)==9:

            for d in range(1,10):

                if pan_check.count(str(d))==1:
                    continue

                else:
                    break

            else:

                if c not in prod_list:                        
                        prod_list += [c]
                        prod_sum += c
                        
                else:
                    pass
                
print(prod_sum)
