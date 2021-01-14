#Euler Project Problem 45
tlist=[]
plist=[]
hlist=[]


for a in range(1,100000):

    t=int(a*(a+1)/2)
    p=int(a*(3*a-1)/2)
    h=int(a*(2*a-1))

    tlist=tlist+[t]
    plist=plist+[p]
    hlist=hlist+[h]

    if t in plist and t in hlist:

        print(t)
