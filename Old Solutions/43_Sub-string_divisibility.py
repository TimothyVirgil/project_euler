#Euler Project Problem 43: Sub-string divisibility

#Need to find pandigitals
#Need to check divisibility for different digit ranges

panList=[]
specpansum=0

for q in range(1023456789,9876543210):

    if q%1000000==0:
        print('working')

    jill=str(q)

    if int(jill[3])%2!=0:
        continue
    if int(jill[5])!=0 and int(jill[5])!=5:
        continue
    for g in range(0,10):
        if jill.count(str(g))!=1:
            break
        if g==9:
            panList=panList+[q]


for r in panList:

    jack=str(r)

    if int(jack[1:4])%2!=0 or int(jack[2:5])%3!=0 or int(jack[3:6])%5!=0 or int(jack[4:7])%7!=0 or int(jack[5:8])%11!=0 or int(jack[6:9])%13!=0 or int(jack[7:10])!=0:
        continue

    else:
        specpansum=specpansum+r
                                                                                                                                                    

print(specpansum)        
