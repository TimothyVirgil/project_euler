#Project Euler Problem 21: Mark 2

import math

totSum=0

for a in range(220,10000):
    aSum=1
    cSum=1

    for b in range(2,round(math.sqrt(a))+1):

        if b==math.sqrt(a):

            aSum=aSum+b

            if a==aSum:
                break

            for c in range(2,round(math.sqrt(aSum))+1):

                   if c==math.sqrt(aSum):
                       cSum=cSum+c

                       if a==int(cSum):
                           totSum=totSum+a
                   
                   elif c==round(math.sqrt(aSum)):

                       if aSum%c==0:

                           cSum=cSum+c+aSum/c
                           
                           
                           if a==int(cSum):
                               totSum=totSum+a
                               
                       elif a==int(cSum):
                           totSum=totSum+a
                   
                   elif aSum%c==0:
                       cSum=cSum+c+aSum/c
                   
        elif b==round(math.sqrt(a)):

            if a%b==0:

                   aSum=aSum+b+a/b


            if a==int(aSum):
                break
            
                   
            for c in range(2,round(math.sqrt(aSum))+1):

                if c==math.sqrt(aSum):
                       cSum=cSum+c

                       if a==int(cSum):
                           totSum=totSum+a
                   
                elif c==round(math.sqrt(aSum)):
                       if aSum%c==0:

                           cSum=cSum+c+aSum/c

                           if a==int(cSum):
                               totSum=totSum+a
                       elif a==int(cSum):
                           totSum=totSum+a
                   
                elif aSum%c==0:
                       cSum=cSum+c+aSum/c

        elif a%b==0:
                   aSum=aSum+b+a/b

print(totSum)

        
                   
