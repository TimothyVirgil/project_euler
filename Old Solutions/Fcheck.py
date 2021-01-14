#F(n) = the number of integers x<=n that can be written as x=a^2*b^3
#a can equal b
#This program is to ascertain any patterns that may arise.
#The ultimate goal is to find F(9*10^18)
#F(100)=2, F(20000)=130, F(3000000)=2014

fList=[]
f=0
gList=[]
hList=[]
fifthList=[]


for a in range(2,3536):

    for b in range(2,293):

        f=a**2*b**3

        if f<=100000000 and f not in gList:

            gList=gList+[f]

            
            fList=fList+[(f, a, b)]

        if f>100000000:

            break

gList = sorted(fList, key = lambda q:q[2])

    
for x in gList:
    print(x)
   


print(len(fList))


    
