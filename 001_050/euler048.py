'''Solution to Project Euler Problem 48
Code by Timothy Virgil Payne Jr.
Started: 2/6/22
Completed: 2/6/22
'''

a=0

for b in range(1,1001):
    a += b**b

ser_sum=str(a)

print(ser_sum[-10:])
