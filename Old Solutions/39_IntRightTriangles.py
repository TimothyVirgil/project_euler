#Euler Project Problem 39: Integer Right Triangles

#Need to find solutions for a perimeter that fits pyth theorem

#Need to count solutions

#Need to find highest count
import math
countlist={}
hyplist=[]
perlist=[]
for d in range(1,900):

    for e in range(1,900):

        c=math.sqrt(d**2+e**2)

        if c.is_integer():

            

            if int(c)+d+e>1000:
                break

            if int(c)+d+e not in perlist:
                perlist=perlist+[int(c)+d+e]
                countlist[str(int(c)+d+e)]=1

            else:
                countlist[str(int(c)+d+e)]+=1


joke=list(countlist.values())

clown=list(countlist.keys())

print(clown[joke.index(max(joke))])

print(max(joke))
