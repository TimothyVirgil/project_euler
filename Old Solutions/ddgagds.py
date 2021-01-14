import sys
hand=['2H','2C','3S','6H','TH']
highcard=0
full=0
of=0
highlist=[]
suits = hand[0][1]+hand[1][1]+hand[2][1]+hand[3][1]+hand[4][1]
value = hand[0][0]+hand[1][0]+hand[2][0]+hand[3][0]+hand[4][0]
intvalue=[]
for p in value:
    if p=='J':
        intvalue=intvalue+[11]
        continue
    if p=='T':
        intvalue=intvalue+[10]
        continue
    if p =='Q':
        intvalue=intvalue+[12]
        continue
    if p=='K':
        intvalue=intvalue+[13]
        continue
    if p=='A':
        intvalue=intvalue+[14]
        continue
    else:
        intvalue=intvalue+[int(p)]
    intvalue.sort()   

#Royal Flush

if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and ''.join(sorted(value))=='AJKQT':

    print('Holy Cow! You got a royal flush!')

    
#Straight Flush

if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and intvalue[0]+1==intvalue[1] and intvalue[1]+1==intvalue[2] and intvalue[2]+1==intvalue[3] and intvalue[3]+1==intvalue[4]:

    print('Straight Flush. Very nice.')
    highcard=intvalue[4]

if suits[0]==suits[1]==suits[2]==suits[3]==suits[4] and intvalue[0]==2 and intvalue[1]==3 and intvalue[2]==4 and intvalue[3]==5 and intvalue[4]==14:
    print('Straight Flush. Very nice.')
    highcard=5
    sys.exit()
#Four of a Kind

for a in range(1,15):

    if intvalue.count(a)==4:

        print('Four of a kind! Yikes!')

        for a in range(1,15):

            if intvalue.count(a)==1:

                highcard=a

#Full House
                
for a in range(1,15):

    if intvalue.count(a)==3:

        for b in range(1,15):

            if a==b:
                continue

            elif intvalue.count(b)==2:

                print('Full House. Classic.')

                full=a
                of=b



#Flush
                    
if suits[0]==suits[1]==suits[2]==suits[3]==suits[4]:

    print('Flush. Nice hand.')
    
    highcard=intvalue[4]
    print(highcard)

  #Straight

if intvalue[0]+1==intvalue[1] and intvalue[1]+1==intvalue[2] and intvalue[2]+1==intvalue[3] and intvalue[3]+1==intvalue[4]:
    print('Straight. Not bad.')
    highcard=intvalue[4]

if intvalue[0]==2 and intvalue[1]==3 and intvalue[2]==4 and intvalue[3]==5 and intvalue[4]==14:

        print('Straight. Not bad.')
        highcard=5

#Three of a Kind


for a in range(1,15):

    if intvalue.count(a)==3:

        print('Three of a Kind.')

        for p in range(1,15):

            if p==a:
                continue

            else:

                if p in intvalue and p>highcard:
                    highcard=p

        print(highcard)        

        sys.exit()

#Two Pair

for a in range(1,15):

    if intvalue.count(a)==2:

        for b in range(1,15):

            if b==a:
                continue

            if intvalue.count(b)==2:

                print("Two Pair.")

                lowpair=a
                highpair=b

                for g in intvalue:

                    if g==a or g==b:
                        continue
                    else:
                        highcard=g
                        print(highcard)
                        print(lowpair)
                        print(highpair)
                        sys.exit()

#One Pair

for a in range(1,15):

    if intvalue.count(a)==2:

        print('One pair. Better than nothing.')

        for f in intvalue:

            if f==a:
                continue

            else:

                highlist=highlist+[f]

        highcard=highlist[2]
        highcard1=highlist[1]
        highcard2=highlist[0]
        pair=a

        print(highcard,highcard1,highcard2,pair)

            
