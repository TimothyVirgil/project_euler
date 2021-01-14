#Euler Project 60: Prime Pairs

##The primes 3, 7, 109, and 673, are quite remarkable.
## By taking any two primes and concatenating them in 
##any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

##Find the lowest sum for a 
##set of five primes for which 
##any two primes concatenate to produce another prime.


import math
import os

primes=[2,3,5,7,11,13]

def primestest(a):
        for b in range(3,int(math.sqrt(a))+1):

                if a%b==0:
                        return False

                if b==int(math.sqrt(a)):
                        return True



for a in range(17, 10000, 2): #classic prime generator

	for b in range(3,int(math.sqrt(a))+1):

		if a%b==0:
			break

		if b==int(math.sqrt(a)):
			primes=primes+[a]
print(len(primes))


# check for prime pairs

posslist=[]

for a in range(len(primes)):

        clock=str(primes[a])

        for p in range(a+1,len(primes)):

                quack = str(primes[p])

                if primestest(int(clock+quack))  and primestest(int(quack+clock)):

                        for c in range(p+1,len(primes)):
                                king=clock
                                jester=quack
                                bob=str(primes[c])

                                if primestest(int(king+bob)) and primestest(int(bob+king)) and primestest(int(jester+bob)) and primestest(int(bob+jester)):

                                        for g in range(c+1,len(primes)):

                                                duck=str(primes[g])

                                                if primestest(int(king+duck))and primestest(int(duck+king)) and primestest(int(jester+duck)) and primestest(int(duck+jester)) and primestest(int(bob+duck)) and primestest(int(duck+bob)):
                                                        print(clock,quack,bob,duck)


                                                        for f in range(g+1,len(primes)):

                                                                pond=str(primes[f])

                                                                if primestest(int(king+pond)) and primestest(int(pond+king)) and primestest(int(pond+jester)) and primestest(int(jester+pond)) and primestest(int(pond+duck)) and primestest(int(duck+pond)) and primestest(int(bob+pond)) and primestest(int(pond+bob)):
                                                                        print('SUCCCESSSSS',king,quack,bob,duck,pond)

                                                

                                
                
           

##check to see if they concatenate with 3 and 7
##posslist=[]

##for c in primes:
##
##	joke=str(c)
##
##	if primestest(int('3'+joke))  and primestest(int('7'+joke)) and primestest(int(joke+'3'))  and primestest(int(joke+'7')):
##
##		posslist=posslist+[c]		
##
##print((posslist))
##
##poss2list=[]
##
##for x in range(0,len(posslist)):
##
##        jester=str(posslist[x])
##
##        for q in range(x+1,len(posslist)):
##
##                king=str(posslist[q])
##
##                if primestest(int(jester+king))  and primestest(int(king+jester)):
##
##                        print(jester,king)
##
##                        for quack in posslist:
##                                bob=str(quack)
##
##                                if primestest(int(king+bob)) and primestest(int(bob+king)) and primestest(int(jester+bob)) and primestest(int(bob+jester)):
##
##                                        print(bob,king,jester)
##
##print(poss2list)

