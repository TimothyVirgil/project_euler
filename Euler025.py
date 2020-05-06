'''Solution to Project Euler Problem 25
Code by Timothy Virgil Payne Jr.
Started: 5/6/2020
Completed: 5/6/2020
Straightforward solution. Five minutes.
'''

a = 1
b = 2
c = 2
d = str(b)
    
while len(d) < 1_000:
    a , b, c, d = b , a + b, c + 1, str(b)

else:        
    print(c)
    
