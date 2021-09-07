#Euler Project 40: Largest Pandigital Prime

import math

jill=''
currlarge=0

for a in range(7000001,8000000,2):

    jill=str(a)

    if int(jill[-1])==5:
        continue

    elif '0' in jill or '8' in jill:
        continue
    
    for c in range(1,8):
        if jill.count(str(c))!=1:
            break

        if c==7:
            for b in range(2,int(math.sqrt(a))+1):

                if a%b==0:
                    break

                if b==int(math.sqrt(a)):

                    if a>currlarge:
                        currlarge=a
print(currlarge)
            
        

    

            


print(currlarge)

            
