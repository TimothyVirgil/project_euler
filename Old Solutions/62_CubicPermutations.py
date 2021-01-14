#Project Euler 62: Cubic Permutations

from itertools import permutations


def cuberoot(a):

    bozo=a**(1./3.)

    if bozo.is_integer():

        return True

cubelist=[]


johnlist=[]

for x in range(0,15000):    
       
    bozo=x**3

    jack=str(bozo)

    cubelist=cubelist+[jack]

print('found cubes')

jokelist=[]
for quick in cubelist:

    burp=str(quick.count('0'))+str(quick.count('1'))+str(quick.count('2'))+str(quick.count('3'))+str(quick.count('4'))+str(quick.count('5'))+str(quick.count('6'))+str(quick.count('7'))+str(quick.count('8'))+str(quick.count('9'))

    jokelist=jokelist+[burp]
duck=0
for p in range(0,len(jokelist)):
    if duck==4:                                                                                                                                                                                                      
        print(cubelist[p-1])
    duck=0
    for g in range(p+1,len(jokelist)):
                                                                                                                                                                                                                                                                                                                                                                                                                       
        if jokelist[p]==jokelist[g]:
            duck=duck+1                                                                                                                                                                                                 

##duck=0
##for h in cubelist:
##
##    if duck==5:
##        print(johnlist)
##    duck=0
##    print(h)
##            
##    john=list(permutations(h,len(h)))
##
##
##
##    for b in john:
##
##    
##        tony=''
##
##        for c in range(0,len(b)):
##
##            tony=tony+''.join(b[c])
##
##            if c==len(b)-1:
##            
##                johnlist=johnlist+[(tony)]
##
##        for q in johnlist:
##
##            if cuberoot(int(q)):
##
##                duck=duck+1
##
##            
              


    


