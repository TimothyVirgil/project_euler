#F(n) = the number of integers x<=n that can be written as x=a^2*b^3
#a can equal b
#This program is to ascertain any patterns that may arise.
#The ultimate goal is to find F(9*10^18)
#F(100)=2, F(20000)=130, F(3000000)=2014

fList=[]
f=0
gList=[]
hList=[]
fifthList=[]

import time
start_time = time.time()

for b in range(225*10**4,1,-1):

    if b%1000==0:

        print(str(b)+' runs left.')

    for a in range(2,1125*10**6):

    

        f=a**2*b**3

        if f<=9*10**18 and f not in gList:

            gList=gList+[f]

            
            fList=fList+[(f, a, b)]

        if f>9*10**18:

            break


   


print(len(fList))

elapsed_time = time.time() - start_time
print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))




    
