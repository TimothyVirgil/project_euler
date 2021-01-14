#Euler 58

#one is in the middle
#the corners of the spiral can be defined explicitly

#need to capture side length
#need to count primes
#need to count total diagonals

import math
import sys

primediagonals=[3,5,7]  #list of primes in the diagonal, first 3 manual to make algorithm more efficient

for a in range(1,100000):

    sidelength=2*a+1 #side length
    diagnumber=4*a+1 #numbers in diagonal
    botright=int(4*a**2+4*a+1)
    botleft=int(4*a**2+2*a+1)
    topleft=int(4*a**2+1)
    topright=int(4*a**2-2*a+1)

    for b in range(3,int(math.sqrt(botleft)+1)): #prime checker bot left

        if botleft%b==0:
            break

        if b==int(math.sqrt(botleft)):

            primediagonals=primediagonals+[botleft]

    for c in range(3,int(math.sqrt(topleft)+1)): #prime checker top left

        if topleft%c==0:
            break

        if c==int(math.sqrt(topleft)):

            primediagonals=primediagonals+[topleft]

    for d in range(3,int(math.sqrt(topright)+1)): #prime checker top right

        if topright%d==0:
            break

        if d==int(math.sqrt(topright)):

            primediagonals=primediagonals+[topright]

    if (len(primediagonals)/diagnumber) < 0.10: #check ratio, print if below 10%

        print('The side length is: ' + str(sidelength) + '.')
        sys.exit()

    
