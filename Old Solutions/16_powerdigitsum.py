#Project Euler Problem 16 Power digit sum

x = 2**1000

r=0

for p in range(0,len(str(x))):

    r=r+int(str(x)[p])


print(r)

    
