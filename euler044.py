'''Solution to Project Euler Problem 41
Code by Timothy Virgil Payne Jr.
Started: 12/9/21
Completed: 12/30/21
Used pieces of my old solution but made it much faster.'''

def pentest(p):
    n = int(((1 + 24*p) ** 0.5 + 1)/6)   

    if n*(3*n-1)/2 == p:
        return True

    else:
        return False

pentlist=[1]
q = 1
cond = True

while cond:
    q += 1

    n = int((3*q**2-q)/2)

    pentlist.append(n)

    for b in pentlist[:-1]:

        pen1 = n-b
        pen2 = n+b

        if pentest(pen1) and pentest(pen2):

            print(pen1)
            cond = False
            break
