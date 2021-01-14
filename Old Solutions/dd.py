quick=0
quicklist=[]

for a in range(0,20000):

    quick=-3/2*a**2+a/2+1/12

    if quick.is_integer():
        quicklist=quicklist+quick
