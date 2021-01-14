#Euler Project Problem 34: Digit Factorials

import math

joke=0

jokesum=0

jokesumlist=[]

for a in range(3,1000000):

    if joke==(a-1):

        jokesum=jokesum+joke

        jokesumlist=jokesumlist+[joke]

    joke=0

    clown=str(a)

    for b in range(0,len(clown)):

        joke=joke+math.factorial(int(clown[b]))

print(jokesumlist)

print(jokesum)

    
