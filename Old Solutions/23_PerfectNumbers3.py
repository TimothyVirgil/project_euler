#Project Euler #23 Non-abundant sums

#One strategy- find all abundant numbers - list them.
#Create a new list where I add the first to the rest, second the rest,etc.
#create another list for numbers not in list 2 up to 28123

import math

abund=[]
sumabund=[]
notsum=0
asum=0

for a in range(12,28124):

        if a%6==0:
                abund.append(a)
                

        elif asum>(a-1):
                abund.append(a-1)

        

                              

        asum=0

       

        for b in range(2,round(math.sqrt(a))+1):
                if a%6==0:
                        break

                
                elif b==math.sqrt(a):
                    asum=asum+b
                elif a%b==0:
                    asum=asum+b+a/b

print(len(abund))

abund.sort()                      
                        
                            
          
                
for x in range(0,28124):

        for q in range(0,len(abund)):

                if x - abund[q] not in abund:

                        notsum=notsum+x

       
               


print(notsum)
               
               
                
                
