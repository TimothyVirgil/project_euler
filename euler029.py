'''Solution to Project Euler Problem 29
Code by Timothy Virgil Payne Jr.
Started: 1/25/2021
Completed: 1/25/2021

Copied my old straightforward brute force solution

I would need to retool this for higher numbers... but if we have the power.. why bother now?
'''

distList=[]
dist=0

for a in range(2,101):

    for b in range(2,101):

        dist=a**b

        if dist not in distList:

            distList.append(dist)


print(len(distList))
