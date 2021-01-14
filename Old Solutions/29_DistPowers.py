#Euler Project Problem 29: Distinct Powers

distList=[]
dist=0

for a in range(2,101):

    for b in range(2,101):

        dist=a**b

        if dist not in distList:

            distList.append(dist)


print(len(distList))

    
