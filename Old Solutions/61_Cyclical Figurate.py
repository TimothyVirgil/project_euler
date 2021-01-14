#61 Cyclical figurate numbers

import sys

#Triangle 4 dig
Trilist=[]
tri=0
for a in range(45,141):

    tri=int((a**2+a)/2)
    Trilist=Trilist+[str(tri)]


#Square
Squlist=[]
squ=0
for b in range(32,100):

    squ=b**2
    Squlist=Squlist+[str(squ)]


#Pent
Pentlist=[]
pent=0

for c in range(26,82):

    pent=int((c*(3*c-1))/2)
    Pentlist=Pentlist+[str(pent)]

#Hex
Hlist=[]
hexnum=0

for d in range(23,71):

    hexnum=d*(2*d-1)
    Hlist=Hlist+[str(hexnum)]

#Hept

Heplist=[]
hep=0

for e in range(21,64):

    hep=int((e*(5*e-3))/2)
    Heplist=Heplist+[str(hep)]


#Oct

Octlist=[]
octnum=0

for f in range(19,59):

    octnum=f*(3*f-2)
    Octlist=Octlist+[str(octnum)]

from itertools import permutations




posslist=list(permutations(['0','1','2','3','4','5'])) #Only 720 possible permuations and fairly short lists, so brute force is OK!

permslist=[Trilist,Squlist,Pentlist,Hlist,Heplist,Octlist]

for a in posslist:

    for b in permslist[int(a[0])]:

        for c in permslist[int(a[1])]:

            if b[0:2]!=c[2:4]:

                continue

            else:

                for d in permslist[int(a[2])]:

                    if c[0:2]!=d[2:4]:

                        continue

                    else:

                        for e in permslist[int(a[3])]:

                            if d[0:2]!=e[2:4]:

                                continue

                            else:

                                for f in permslist[int(a[4])]:

                                    if e[0:2]!=f[2:4]:
                                        continue

                                    else:

                                        for g in permslist[int(a[5])]:

                                            if f[0:2]==g[2:4] and g[0:2]==b[2:4]:

                                                print(int(b)+int(c)+int(d)+int(e)+int(f)+int(g))
                                                sys.exit()

            



