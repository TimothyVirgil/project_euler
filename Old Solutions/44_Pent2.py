#Euler Project Problem 44: Pentagonal Numbers Try 2

#differences are of the form 3n+1 or 3n+2

#Based on some algebra, n has to be equal to (q^2-q-1)/6 where q is int

nlist=[]

for a in range(0,100000):

   n= a*(3*a-1)/2

   pentlist=pentlist+[n]

   if n%3!=0:
       posslist=posslist+[n]




####mlist=[]
####
####for c in range(0,1000):
####
####    m=(3*c**2-c+2)/6
####
####    if m.is_integer():
####
####        mlist=mlist+[int(
##
##
##
##
##posslist=[]
##pentlist=[]
##
##
##for b in nlist:
##
##    n=b*(3*b-1)/2
##
##    posslist=posslist+[]
##
##print(len(posslist))
##
##
##print('done')
##for d in posslist:
##
##    for p in range(int(d+1),len(posslist)):
##
##        if d + posslist[p] in pentlist and abs(d-posslist[p]) in pentlist:
##
##            print(abs(d-posslist[p]))
##
##            sys.exit




        
