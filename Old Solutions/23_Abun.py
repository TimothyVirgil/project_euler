#Euler Project Problem 23: Abundant Sums

#Step 1: Find Abundant #'s

import math
import time

start=time.time()

abunlist=[]
abun=0
abunsumlist=[]
abunsum=0
abunsumtot=0
notabunsumlist=list(range(0,28123))
notabunsum=0
sumtot=0

for a in range(0,28124):

    sumtot=sumtot+a

print(sumtot)

for a in range(12,28124):

    if abun>(a-1):

        abunlist=abunlist+[a-1]

        for c in range(0,len(abunlist)):

            abunsum = 0

            abunsum = (a-1) + abunlist[c]

            if abunsum>28123:
                break

            if abunsum not in abunsumlist:

                abunsumlist=abunsumlist + [abunsum]

               
               
                       

    abun=1
    
    if a%1000==0:

        current=time.time()

        current=int(current)

        print("It's been " + str(current-start) + ' seconds.')
        print('There are ' + str(len(abunsumlist)) + ' that can be written as sums of abundant numbers.')

    

    for b in range(2,round(math.sqrt(a))+1):

        if a%b==0:
            abun=abun+b+a/b

            if b==math.sqrt(a):
                abun=abun-b



for d in range(0,len(abunsumlist)):

    abunsumtot=abunsumtot+abunsumlist[d]




print('almost done')

abunsumnottot=0

abunsumnottot=sumtot-abunsumtot



print(abunsumnottot)

    



    

      



    





    

    
      




        

    
