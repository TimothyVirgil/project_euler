#Project Euler Problem 21: Amicable Numbers

import math

totSum=0

for a in range(2,10000):

    aSum=a
    cSum=0
    

    for b in range(1,round(math.sqrt(a))+1):

        if b==math.sqrt(a):
            aSum=aSum+b
            
            for c in range(1,round(math.sqrt(aSum))+1):
                if c==math.sqrt(aSum):
                    cSum=cSum+c+aSum

                    if a==cSum:
                        totSum=totSum+a
                elif c==round(math.sqrt(aSum)):
                    cSum=cSum+aSum

                    if aSum%c==0:
                        
                        cSum=cSum+c

                        if a==cSum:
                            totSum=totSum+a
                elif aSum%c==0:
                    cSum=cSum+c

        elif b==round(math.sqrt(a)):

            if a%b==0:

                aSum=aSum+b
            for c in range(1,round(math.sqrt(aSum))+1):
                if c==math.sqrt(aSum):
                    cSum=cSum+c+aSum

                    if a==cSum:
                        totSum=totSum+a
                elif c==round(math.sqrt(aSum)):
                    cSum=cSum+aSum

                    if aSum%c==0:
                        cSum=cSum+c

                        if a==cSum:
                            totSum=totSum+a
                elif aSum%c==0:
                    cSum=cSum+c

        elif a%b==0:
            aSum=aSum+b


print(totSum)
