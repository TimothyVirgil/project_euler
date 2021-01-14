#Euler Project Problem 35: Circular Primes

import math
import itertools
primeslist=[]
circprimeslist=[]
joke=''


def longestWord(letters):
    return [''.join(i) for i in itertools.permutations(letters)]

for a in range(0,100000000):

    if a%1000000==0:

        print('Another 1/100 there!')

   


    for b in range(2,int(math.sqrt(a))+1):

        if a%b==0:

            break

        if b==int(math.sqrt(a)):

            primeslist=primeslist+[a]


print('checking circulars...')

print(len(primeslist))

for c in range(0,len(primeslist)):

    if c%1000==0:

        print("I'm working here...")

    clown=str(primeslist[c])

    for d in range(0,len(clown)-1):

        joke=''        

        for e in range(1,len(clown)+1):

            joke=joke+clown[(d+e)%len(clown)]

        if int(joke) not in primeslist:

            break

        if d==len(clown)-2:

            circprimeslist=circprimeslist+[primeslist[c]]

   

print(len(circprimeslist))

print(circprimeslist)
    



