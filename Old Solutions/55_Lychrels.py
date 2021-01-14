#Euler 55 Lychrel Numbers

#Generate and add palindromes

lychrels=[]

for a in range(10,10000):

    t=0
    init=str(a)
    posspal=init
    pal=''

    while t<50:



        init=posspal
        pal=''

        for b in range(0,int(len(init))):

            pal=pal + init[-1-b]

        posspal=str(int(pal)+int(init))

        

        for b in range(0,len(posspal)//2):      #run through the number.. only need to do half since we go up and down

            if int(posspal[b]) != int(posspal[-b-1]):  #palindrome checker
                t+=1
                break

            if b==(len(posspal)//2)-1:  #if it makes it through the loop, it's a palindrome

                t=51
                break


    if t==50:
        lychrels=lychrels+[a]

    
        

print(len(lychrels))        

    


#Check if answer is palindrome

#if more than 50 iterations, add to list
