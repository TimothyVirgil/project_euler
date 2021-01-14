#Project Euler Problem 27: Quadratic Primes

remList=[]

c=2
import math
import time
start_time = time.time()

form=1

for a in range(-1000,1000):

    if a%100==0:

        print('hi')
        elapsed_time = time.time() - start_time
        print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

    for b in range(-1000,1000):

        form=1

        for n in range(0,10000):

            

            if form==0:

                break

           

            form=n**2+a*n+b

            if form<0:

                break

            
            for c in range(2,int(math.sqrt(form)+1)):

                if form%c==0:

                

                    if n>20:

                        remList=remList+[(n,a,b)]


                    form=0

                    break
                
                
print(sorted(remList, key=lambda q:q[0]))
                    

          
