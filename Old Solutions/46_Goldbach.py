#Euler Project Problem 46: Goldbach's other conjecture

# gen primes
import math
primes=[2,3,5,7]
comps=[]

for a in range(3,10000,2):

    for b in range(3,int(math.sqrt(a))+1):

        if a%b==0:

            comps=comps+[a]

            break

        if b==int(math.sqrt(a)):

            primes=primes+[a]


print(comps)
print(primes)

iscomp=1
    
for x in comps:

    iscomp=0

    for b in primes:

        if iscomp>0:
            break

        if b>x:

            if iscomp==0:
                print(x)
            break
            

        q=math.sqrt((x-b)/2)

        if q.is_integer():

            iscomp+=1

    
            

        
    
