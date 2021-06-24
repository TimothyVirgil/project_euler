'''Solution to Project Euler Problem 30
Code by Timothy Virgil Payne Jr.
Started: 6/23/2021
Completed: 6/24/2021

Modified from an old solution. I actually thought my old solution was bad... but upon reexamining it uses a decent recursion
before I even knew what recursion was.
You can use these functions to find lots of different coin combinations.
For instance, if you wanted to know all the ways to make ten dollars with five pence coins and below,
you could do five_pence(1000).
'''
def two_pence(a):
    L=0
    L=a//2+1
    return(L)

def five_pence(a):
    R=0
    b=a//5
    for c in range(0,b+1):
        R=R+two_pence(a-c*5)
    return(R)

def ten_pence(a):
    Q=0
    b=a//10
    for c in range(0,b+1):
        Q=Q+five_pence(a-c*10)
    return(Q)

def twenty_pence(a):
    P=0
    b=a//20
    for c in range(0,b+1):
        P=P+ten_pence(a-c*20)
    return(P)

def fifty_pence(a):
    G=0
    b=a//50
    for c in range(0,b+1):
        G=G+twenty_pence(a-c*50)
    return(G)

def one_pound(a):
    M=0
    b=a//100
    for c in range(0,b+1):
        M=M+fifty_pence(a-c*100)
    return(M)

def two_pound(a):
    N=0
    b=a//200
    for c in range(0,b+1):
        N=N+one_pound(a-c*200)
    return(N)

print(two_pound(200))
