#Euler Project 47: Distint Prime Factors
import math
import sys

flist=[]
for a in range(10,1000000):

    if len(flist)==4:
        fcount+=1

        if fcount==4:

            print(a-4)
            sys.exit

    else:
        fcount=0

    flist=[]
    b=1
    while b!=0:

        for c in range(2,int(math.sqrt(a)+4)):

            if a%c==0:
                if c not in flist:

                    flist=flist+[c]

                a=a/c
                break

           
            if c==int(math.sqrt(a)+3):

                if a not in flist:

                    flist=flist+[a]

                b=0

                

                

                

    
