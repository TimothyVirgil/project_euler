#Project Euler #23 Non-abundant sums

#One strategy- find all abundant numbers - list them.
#Create a new list where I add the first to the rest, second the rest,etc.
#create another list for numbers not in list 2 up to 28123

import math

abund=[]
sumabund=[]
notsumabund=[]
notsum=0
asum=0

for a in range(12,28124):

        if asum>(a-1):
                abund.append(a-1)

        asum=0

       

        for b in range(2,round(math.sqrt(a))+1):
                if b==math.sqrt(a):
                    asum=asum+b
                elif a%b==0:
                    asum=asum+b+a/b

                       
                        
                                
                 
                
                

for c in range(0,len(abund)):

        for d in range(c,len(abund)):

                sumabund.append(abund[c]+abund[d])


for e in range(0,28124):
        if e not in sumabund:
                notsumabund.append(e)


for f in range(0,len(sumabund)):
        notsum=notsum+sumabund[f]


print(notsum)
               
               
                
                
