#Euler Project Problem 25: 1000-digit Fibonacci number

Fib = 1

FibList=[1,1]

for a in range(1,130000):

    Fib=FibList[a-1]+Fib

    FibList=FibList+[Fib]

    if len(str(Fib))==1000:

        print(len(FibList))

        break

