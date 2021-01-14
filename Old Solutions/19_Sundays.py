#Project Euler Problem 19 Counting Sundays

#n = number of Sundays that are the first of the month (I already counted 1900)
#s = current starting day (1901 starts on a Tuesday)

n=1
s=2

for a in range(1,26):

    for b in range(1,5):

        if b==4:
            s=s+3
            if s%7==0:
                n=n+1
            s=s+1
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
        else:
            s=s+3
            if s%7==0:
                n=n+2
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1
            s=s+2
            if s%7==0:
                n=n+1
            s=s+3
            if s%7==0:
                n=n+1

print(n)
                
