#Project Euler Problem 14 Longest Collatze Sequence

p=2
a=[]

for x in range(2,1000000):

    if len(a)>p:

        p=len(a)

        print(x-1)
          
    
    a=[]
    
    while x>1:

        if x%2==0:
            x=x/2

            a=a+[x]

        else:
            x=3*x+1

            a=a+[x]
