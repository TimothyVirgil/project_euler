#Euler Project Problem 37

#Need to check for primes

#Need to check to see if it's truncated

#1st digit must be 2,3,5,7

#middle digits must be 1,3,7,9

#last digit must be 3 or 7

import math

trunkprimes=[23,37,73,53]
trunksum=0

for num in range(101,1000000000,2):

    if len(trunkprimes)==11:

        for q in trunkprimes:
            trunksum=trunksum+q
            

        print(trunkprimes)
        print(trunksum)

        break


    bob=str(num)

    if int(bob[-1])!=3 and int(bob[-1])!=7:
           continue

    if int(bob[0])!=2 and int(bob[0])!=3 and int(bob[0])!=5 and int(bob[0])!=7:
           continue

    if len(bob)>2:
        if '0' in bob[1:] or '2' in bob[1:] or '4' in bob[1:] or '5' in bob[1:] or '6' in bob[1:] or '8' in bob[1:]: 
            continue
       
    for a in range(2,int(math.sqrt(num))+1):

        if num%a==0:
                break

        if a==int(math.sqrt(num)):

            jes=3
            c=2

            for q in range(1,len(bob)):

                if jes%c==0:
                    break

                jes=int(bob[q:])

                for c in range(2,int(math.sqrt(jes))+2):

                    if jes%c==0:
                        break
                    if c>=int(math.sqrt(jes)):
                        qes=int(bob[:-q])

                        for d in range(2,int(math.sqrt(qes))+2):
                            if qes%d==0:
                                jes=c+1
                                break
                                
                            if d>=int(math.sqrt(qes)) and q==len(bob)-1 and num not in trunkprimes:

                                trunkprimes=trunkprimes+[num]



                

                

                

    


    
