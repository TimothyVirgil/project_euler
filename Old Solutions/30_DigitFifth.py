#Euler Project Problem 30: Digit fifth powers
#Cool program that finds numbers that can are the sum of the fifths
#of their digits

goo=0
fifList=[]
fifSum=0

for b in range(1000000):

    if goo==(b-1):

        fifList=fifList+[b-1]

    bob=str(b)

    goo=0

    for q in range(0,len(bob)):

        goo=goo+int(bob[q])**5

print(fifList)

for a in fifList:

    fifSum=fifSum+a

print(fifSum)

        
