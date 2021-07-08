sumprodList=[]
sumprod=0

for a in range(0,100):

    for b in range(0,10000):

        c=a*b

        clown=str(a)+str(b)+str(c)

        if len(clown)==9:

            if clown.count('1')==1 and clown.count('2')==1 and clown.count('3')==1 and clown.count('4')==1 and clown.count('5')==1 and clown.count('6')==1 and clown.count('7')==1 and clown.count('8')==1 and clown.count('9')==1:


                print(a,b,c)

                if c not in sumprodList:

                    sumprodList=sumprodList + [c]

                    sumprod=sumprod+c


print(sumprodList)

print(sumprod)

                
