#project euler 38 self powers:

b=0

for a in range(1,1001):

    b=b+a**a

bob=str(b)

print(bob[-10:])
