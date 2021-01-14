#Euler 57 Square Root Convergents

#Found a simple algorithm for root 2 numerators and denominators

prevnum=7
prev2num=3
prevden=5
prev2den=2

numgreater=0

for a in range(0,998):

    currden=prevden*2+prev2den

    currnum=prevnum*2+prev2num

    if len(str(currnum))>len(str(currden)):

        numgreater+=1

    prev2den=prevden

    prevden=currden

    prev2num=prevnum

    prevnum=currnum
    


    


print(numgreater)

    
