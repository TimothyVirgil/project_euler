#Euler 63 Powerful digit counts

diglist=[1,2,3,4,5,6,7,8,9,16,25,36,49,64,81,125,216,343,512,729]

#generate powers

for a in range(0,100):

    for b in range(0,50):

        bozo=b**a

        if bozo<(10**(a-1)):
            continue
        if bozo>=(10**a):
            break
        else:
            if bozo not in diglist:
                diglist=diglist+[bozo]

print(len(diglist))



##for a in range(0,10000):
##
##    bozo=a**4
##
##    if bozo<1000:
##        continue
##    if bozo>=10000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##        
##
##for a in range(0,10000):
##
##    bozo=a**5
##
##    if bozo<10000:
##        continue
##    if bozo>=100000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##for a in range(0,10000):
##
##    bozo=a**6
##
##    if bozo<100000:
##        continue
##    if bozo>=1000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##for a in range(0,10000):
##
##    bozo=a**7
##
##    if bozo<1000000:
##        continue
##    if bozo>=10000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##
##for a in range(0,10000):
##
##    bozo=a**8
##
##    if bozo<10000000:
##        continue
##    if bozo>=100000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##
##for a in range(0,10000):
##
##    bozo=a**9
##
##    if bozo<100000000:
##        continue
##    if bozo>=1000000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##
##for a in range(0,10000):
##
##    bozo=a**10
##
##    if bozo<1000000000:
##        continue
##    if bozo>=10000000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##for a in range(0,10000):
##
##    bozo=a**10
##
##    if bozo<1000000000:
##        continue
##    if bozo>=10000000000:
##        break
##    else:
##        if bozo not in diglist:
##            diglist=diglist+[bozo]
##
##
##print(len(diglist))
