#Project Euler Problem 44 Pentagon Numbers
import sys
Pentlist=[]
pent=0
for q in range(1,1000000):

    if q%1000==0:

        print('hi')

    pent=int(q*(3*q-1)/2)
    Pentlist=Pentlist+[pent]


print('done')

for b in range(1,1000):

    a=Pentlist[3*b+1]
    c=Pentlist[int((b/2)*(9*b+5))]

    if int(abs(a-c)) in Pentlist:

        print(int(abs(a-c)))
        sys.exit

        


##    for g in range(0,len(Pentlist)):
##
##        for k in range(g,len(Pentlist)):
##
##            if abs(Pentlist[g]-Pentlist[k])!=0 and abs(Pentlist[g]-Pentlist[k]) in Pentlist and Pentlist[g]+Pentlist[k] in Pentlist:
##
##                print(abs(Pentlist[g]-Pentlist[k]))
##
##                sys.exit()
