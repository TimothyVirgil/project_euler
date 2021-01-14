#Euler Project Problem 28: Number spiral diagonals

asum=1
num=1

for a in range(1,501):

    for b in range(0,4):

        num=num+2*a
        

        asum=asum+num

print(asum)
