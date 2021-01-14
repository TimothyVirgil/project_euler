#Euler Problem 56 - under a second using common sense constraints

highsum=0


for a in range(99,60,-1):    

    for b in range(99,90,-1):

        currsum=0
        
        c=a**b

        num=str(c)

        for q in range(0,len(num)):

            currsum=currsum+int(num[q])

            if q==len(num)-1 and currsum>highsum:

                highsum=currsum

                print('new high')

print(highsum)
                                
