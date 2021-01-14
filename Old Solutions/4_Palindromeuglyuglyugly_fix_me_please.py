

for bozo in range(100,1000):
    for clown in range(100,1000):
        maybepal = bozo*clown
        str(maybepal)
        if len(str(maybepal))==6:
            if str(maybepal)[0]==str(maybepal)[-1]:
                if str(maybepal)[1]==str(maybepal)[-2]:
                    if str(maybepal)[2]==str(maybepal)[-3]:
                        print(str(maybepal) + ' is a palindrome.')
       
                
                
    
