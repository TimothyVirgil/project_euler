import sys

pentlist=[]

for q in range(1,1000000000):
    n=int((3*q**2-q)/2)

    pentlist=pentlist+[n]

    for b in pentlist:

        if n-b in pentlist and int(abs(2*b-n)) in pentlist:

            print(int(abs(2*b-n)))

    

    print(q,n)



##    for g in pentlist:
##
##        if n - g in pentlist:
##
##            if abs(2*g-n) in pentlist:
##
##                print(abs(2*g-n))
##
##                sys.exit

    
