#Euler Project Problem 38: Pandigital Multiples

#Need to multiply until I get 9 digits, check for repeats
currjill=0

for a in range(1,10000000):

    

    bob=str(a)

    if int(bob[0])!=9:
        continue

    jack=0
    jill=''

    for b in range(1,6):

        jack=b*a

        jill=jill+str(jack)

        if len(jill)<9:
            continue

        if len(jill)>9:
            break

        if len(jill)==9:

            for b in range(1,10):
                
                if jill.count(str(b))!=1:
                    break

                if b==9:
                    if int(jill)>currjill:
                        currjill=int(jill)
                        print(currjill)

                    break

          
        
print(currjill)
  
