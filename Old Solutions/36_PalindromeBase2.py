#Euler Project Problem 36: Double-base palindromes

#First Task: Check for palindromes DONE

#Need to make sure first=last, second=second to last, etc. for odd lengths,
#middle is unimportant

palList=[1,2,3,4,5,6,7,8,9]    #one digit palindromes

for a in range(1,1000000,2):    #loop to one million, only need to check odds

    d=str(a)               #convert to string for index purposes

    for b in range(0,len(d)//2):      #run through the number.. only need to do half since we go up and down

        if int(d[b]) != int(d[-b-1]):  #palindrome checker
            break

        if b==(len(d)//2)-1:  #if it makes it through the loop, it's a palindrome

            palList=palList+[a]


print(palList[0:200])

#SECOND TASK: Convert to base 2


gar=''
bothpalList=[]

for x in palList:

   

    pal = x
    gar =''

    for z in range(19,-1,-1):   #run through powers of 2 up to 19 (2^20 is over one mil)


        if pal>=2**z:
            pal=pal-2**z
            gar=gar+str(1)  # 1 in the place value

        elif len(gar)==0:  #can't start with a 0
            continue

        elif pal<2**z:
            gar = gar + str(0)  # 0 in the place value

        if z==0: #Time to check to see if the base 2 is a palindrome
           

            for r in range(0,len(gar)//2):      #doesn't work for 1 run through the number.. only need to do half since we go up and down

                    if int(gar[r]) != int(gar[-r-1]):  #palindrome checker
                        break

                    if r==(len(gar)//2)-1:  #if it makes it through the loop, it's a palindrome

                        bothpalList=bothpalList+[int(x)]

#time to sum up
palsum=1  #algorithm above doesn't work for 1
for t in bothpalList:
    palsum=palsum+t


print(palsum)

    
