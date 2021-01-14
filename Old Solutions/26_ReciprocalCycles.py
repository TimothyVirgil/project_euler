#Euler Project Problem 26: Reciprocal Cycles

#Write an algorithm to capture repeating decimal lengths

#We keep seeing if there the number divides into a power of ten.

#If a remainder repeats, we have found a repeating decimal

cycleTuple=()
cycleTupleList=[]

for d in range(2,5000):
    

    rList=[]

    for b in range(1,10000):

        if 10**b%d==0:
            break

        else:
            if 10**b%d in rList:

                cycleTupleList=cycleTupleList+[(d, len(rList))]
                
                break

            rList=rList+[10**b%d]


print(sorted(cycleTupleList, key=lambda q:q[1]))


            
            

        

