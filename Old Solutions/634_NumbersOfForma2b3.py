#Euler Project Problem 634: Numbers of the form a^2*b^3

import math
f=0
b=0
fList=[]

import time

start=time.time()

for a in range(2,(800000)):

    if a%10==0:
        print('hi')

    for b in range(2,(8000000)):

        f=a**2*b**3

        
        if f<=(8000000) and f not in fList:

            fList=fList+[f]

        if f>(8000000):

            break

print(len(fList))

    
    
