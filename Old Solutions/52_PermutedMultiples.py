#Euler Project 52

onecount=0
twocount=0
threecount=0
fourcount=0
fivecount=0
sixcount=0
sevencount=0
eightcount=0
ninecount=0
zerocount=0

for p in range(1,1000000):
    duck=0
    joke=str(p)
    onecount=joke.count('1')
    twocount=joke.count('2')
    threecount=joke.count('3')
    fourcount=joke.count('4')
    fivecount=joke.count('5')
    sixcount=joke.count('6')
    sevencount=joke.count('7')
    eightcount=joke.count('8')
    ninecount=joke.count('9')
    zerocount=joke.count('0')

    for x in range(2,7):

        quack=str(p*x)

        if quack.count('1')!=onecount or quack.count('2')!=twocount or quack.count('3')!=threecount or quack.count('4')!=fourcount or quack.count('5')!=fivecount or quack.count('6')!=sixcount or quack.count('7')!=sevencount or quack.count('8')!=eightcount or quack.count('9')!=ninecount or quack.count('0')!=zerocount:
            break

        else:
            duck+=1

            if duck==5:

                print(p)

       
