def Lap(a):

    L=0

    L=a//2+1

    return(L)

def Rap(a):

    R=0

    b=a//5

    for c in range(0,b+1):

        R=R+Lap(a-c*5)

    return(R)

def Qap(a):

    Q=0

    b=a//10

    for c in range(0,b+1):

        Q=Q+Rap(a-c*10)

    return(Q)


def Pap(a):

    P=0

    b=a//20

    for c in range(0,b+1):

        P=P+Qap(a-c*20)

    return(P)


def Gap(a):

    G=0

    b=a//50

    for c in range(0,b+1):

        G=G+Pap(a-c*50)

    return(G)



def Map(a):

    M=0

    b=a//100

    for c in range(0,b+1):

        M=M+Gap(a-c*100)

    return(M)


def Nap(a):

    N=0

    b=a//200

    for c in range(0,b+1):

        N=N+Map(a-c*200)

    return(N)



print(Nap(200))
