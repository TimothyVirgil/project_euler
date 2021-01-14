#This is a program to find the sum of primes under two million

import math

sumPrimes = 10

for number in range(7,2000000,2):

    for test in range(3,int(round(math.sqrt(number)))+2,2):

        if int(str(number)[-1])==5:
            break
        
        elif test==math.sqrt(number):
            break

        elif test==int(round(math.sqrt(number))):
            sumPrimes = sumPrimes + number
        elif test==int(round(math.sqrt(number))+1):
            sumPrimes = sumPrimes + number

        elif number%test==0:
            break

print(str(sumPrimes))
