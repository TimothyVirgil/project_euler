#Project Euler 50!!!!

import math

primes=[2,3]

for a in range(2,1000000):

    

    for b in range(2,int(math.sqrt(a))+3):

        if a%b==0:

            break

        if b==int(math.sqrt(a)+2):

            primes=primes+[a]


print(primes[0:10])

b=0
boze=0
c=0
joke=0
for p in range(0,len(primes)):
    clock=0
    b=0
    

    for q in range(p,len(primes)):
        
        if b>1000000:
            if joke>boze:
                boze=joke
                print(c,boze)
            break

        b=b+primes[q]
        clock+=1
        if b in primes:
            c=b
            joke=clock

        
        
            
            
            


print(boze)


