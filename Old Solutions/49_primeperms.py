#Euler 49 Prime Perms

#4 digit primes:
import math
fourprimes=[]
for b in range(1001,10000,2):

    for q in range(2,int(math.sqrt(b)+3)):

        if b%q==0:

            break

        if q==int(math.sqrt(b)+2):

            fourprimes=fourprimes+[b]

print('done')

print(len(fourprimes))

for b in range(0,len(fourprimes)):

    for c in range(b+1,len(fourprimes)):

        if int(((fourprimes[b]+fourprimes[c])/2)) in fourprimes:

            bob=sorted(str(fourprimes[b]))
            clown=sorted(str(fourprimes[c]))
            joke=sorted(str(int((fourprimes[b]+fourprimes[c])/2)))

            if bob == joke == clown:

                print(fourprimes[b],int((fourprimes[b]+fourprimes[c])/2),fourprimes[c])
