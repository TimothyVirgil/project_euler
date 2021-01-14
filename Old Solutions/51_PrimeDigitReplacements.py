#Project Euler 51: Prime Digit Replacements


#Notes: This code was ugly. I had to check the screen while it printed out to check for primes.
#I got lucky.
#I am proud of myself though for discovering the idea of multiplying the digits by 1's.
#Not sure why it took me so long... I literally had to remember that computers
#think in binary...

#Know: last digit won't change

#

#Want to Know:

#Notes:

import math

end1=[]
end3=[]
end7=[]
end9=[]
int1=[]
int3=[]
int7=[]
int9=[]
for a in range(100001,1000001,2):

    for b in range(3,int(math.sqrt(a))+1):

        if a%b==0:

            break

        if b==int(math.sqrt(a)):

            joke=str(a)

            if joke[-1]=='1':

                end1=end1+[joke]
                int1=int1+[a]

            if joke[-1]=='3':

                end3=end3+[joke]
                int3=int3+[a]

            if joke[-1]=='7':

                end7=end7+[joke]
                int7=int7+[a]

            if joke[-1]=='9':

                end9=end9+[joke]
                int9=int9+[a]

print('Ones: ' + str(len(end1)))
print('Threes: ' + str(len(end3)))
print('Sevens: ' + str(len(end7)))
print('Nines: ' + str(len(end9)))

success=0

checks=[10,110,100,1110,1100,1000,1010,11110,11100,11000,11010,10110,10100,10010,10000,111110,111100,111000,110000,110100,110010,110110,111010,101110,101010,101100,101000,100100,100110,100010,100000]

for a in range(0,len(int3)):
    

    test=int3[a]


    for p in range(0,len(checks)):

        if success>=8:

              print(int3[a], checks[p-1])

        success=0
              

        for b in range(0,10):

            job=test+b*checks[p]

            if job in int3:

                success+=1
              
              


    


    


    




    
