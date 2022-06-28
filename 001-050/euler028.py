'''Solution to Project Euler Problem 28
Code by Timothy Virgil Payne Jr.
Started: 1/25/2021
Completed: 1/25/2021

I copied my old solution verbatim. There's a simple pattern here.
'''

asum=1
num=1

for a in range(1,501):

    for b in range(0,4):

        num=num+2*a
        

        asum=asum+num

print(asum)
