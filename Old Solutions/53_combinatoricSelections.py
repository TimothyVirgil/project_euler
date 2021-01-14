#Euler 53: Combinatoric selections

import math

clock=0

for n in range(23,101):

    for r in range(1,n):

        pop=((int(math.factorial(n))/((int(math.factorial(r))*int(math.factorial(n-r))))))

        if pop>1000000:

            clock+=1


print(clock)

                                     
