pentlist=[]
import sys
import time

start=time.time()
for p in range(1,100000000):

    if p%10000==0:
        print('another 10,000 checked! Learn how to write better code!')

    x=(3*p**2-p)/2

    pentlist=pentlist+[int(x)]

    for q in pentlist:

        if x - q in pentlist and 2*q-x in pentlist:

            print(2*q-x)

            print(time.time()-start)

            sys.exit


