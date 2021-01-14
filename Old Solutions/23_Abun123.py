#Euler Project Problem 23: Abundant Sums

#Step 1: Find Abundant #'s

import math

abunlist=[]
abun=0
abunsumlist=[]
abunsum=0
notabunsum=0

for a in range(12,28123):

    if abun>(a-1):

        abunlist=abunlist+[a-1]

    abun=1

    for b in range(2,round(math.sqrt(a))+1):

        if a%b==0:
            abun=abun+b+a/b

            if b==math.sqrt(a):
                abun=abun-b


for a in range(0,len(abunlist)):

    print(a)

    for b in range(a+1,len(abunlist)):

        abunsum=0

        abunsum=abunlist[a]+abunlist[b]

        if abunsum not in abunsumlist and abunsum<=28123:

            abunsumlist=abunsumlist + [abunsum]

           



for a in range(0,len(abunsumlist)):

    if abunsumlist[a] in notabunsumlist:

        notabunsumlist.remove(abunsumlist[a])

print(len(notabunsumlist))


for a in range(0,len(notabunsum)):

    notabunsum = notabunsum + notabunsumlist[a]

print(notabunsum)


    

      



    





    

    
      




        

    
