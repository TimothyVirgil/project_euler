#Euler Project Prob 43: Quicker Version

#generate multiplese

amult=0
mult2=['002','004','006','008']

for a in range(5,500):

    amult=a*2
    mult2=mult2+[str(amult)]

bob=''

for g in range(0,len(mult2)):

    if len(mult2[g])<3:
        bob='0'+mult2[g]
        mult2[g]=bob

mult3=['003','006','009']
for b in range(4,334):

    amult=b*3
    mult3=mult3+[str(amult)]

for g in range(0,len(mult3)):

    if len(mult3[g])<3:
        bob='0'+mult3[g]
        mult3[g]=bob

mult5=['005']

for c in range(2,200):

    amult=c*5
    mult5=mult5+[str(amult)]

for g in range(0,len(mult5)):

    if len(mult5[g])<3:
        bob='0'+mult5[g]
        mult5[g]=bob


mult7=['007']

for d in range(2,143):
    amult=d*7
    mult7=mult7+[str(amult)]

for g in range(0,len(mult7)):

    if len(mult7[g])<3:
        bob='0'+mult7[g]
        mult7[g]=bob

mult11=[]
for e in range(1,91):
    amult=e*11
    mult11=mult11+[str(amult)]

for g in range(0,len(mult11)):

    if len(mult11[g])<3:
        bob='0'+mult11[g]
        mult11[g]=bob

mult13=[]
for f in range(1,77):
    amult=f*13
    mult13=mult13+[str(amult)]

for g in range(0,len(mult13)):

    if len(mult13[g])<3:
        bob='0'+mult13[g]
        mult13[g]=bob
mult17=[]
for h in range(1,59):

    amult=h*17
    mult17=mult17+[str(amult)]

for g in range(0,len(mult17)):

    if len(mult17[g])<3:
        bob='0'+mult17[g]
        mult17[g]=bob

mult2a=mult2.copy()
for a in mult2:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult2a.remove(a)

            break

mult2b=mult2a.copy()

for a in mult2a:
    quack=int(a)

    if quack%2!=0:
        mult2b.remove(a)



mult3a=mult3.copy()
for a in mult3:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult3a.remove(a)

            break

mult3b=mult3a.copy()

for a in mult3a:
    quack=int(a)

    if quack%3!=0:
        mult3b.remove(a)

mult5a=mult5.copy()
for a in mult5:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult5a.remove(a)

            break

mult5b=mult5a.copy()

for a in mult5a:
    quack=int(a)

    if quack%5!=0:
        mult5b.remove(a)

mult7a=mult7.copy()
for a in mult7:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult7a.remove(a)

            break

mult7b=mult7a.copy()

for a in mult7a:
    quack=int(a)

    if quack%7!=0:
        mult7b.remove(a)

mult11a=mult11.copy()
for a in mult11:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult11a.remove(a)

            break

mult11b=mult11a.copy()

for a in mult11a:
    quack=int(a)

    if quack%11!=0:
        mult11b.remove(a)

mult13a=mult13.copy()
for a in mult13:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult13a.remove(a)

            break

mult13b=mult13a.copy()

for a in mult13a:
    quack=int(a)

    if quack%13!=0:
        mult13b.remove(a)
        
mult17a=mult17.copy()
for a in mult17:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            mult17a.remove(a)

            break

mult17b=mult17a.copy()

for a in mult17a:
    quack=int(a)

    if quack%17!=0:
        mult17b.remove(a)


list2and3=[]




for b in mult2b:

    for q in mult3b:

        if b[1:3]!=q[0:2]:

            continue
        else:
            list2and3=list2and3+[b+q[2]]
            
print(len(list2and3))
list2and3a=list2and3.copy()
for a in list2and3:

    jill=a
    for b in range(0,10):
        
        if jill.count(str(b))>1:
            list2and3a.remove(a)

            break

print(len(list2and3a))

mult2and3=list2and3a
mult235=[]
for a in mult2and3:

    for b in mult5b:

        if a[2:4]!=b[0:2]:
            continue
        else:
            mult235=mult235+[a+b[2]]

mult235a=mult235.copy()

print(len(mult235))

for a in mult235:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            mult235a.remove(a)

            break

print(len(mult235a))

mult2357=[]
for a in mult235a:

    for b in mult7b:

        if a[3:5]!=b[0:2]:
            continue

        else:
            mult2357=mult2357+[a+b[2]]

mult2357a=mult2357.copy()

for a in mult2357:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            mult2357a.remove(a)

            break

mult235711=[]

for a in mult2357a:

    for b in mult11b:

        if a[4:6]!=b[0:2]:
            continue

        else:
            mult235711=mult235711+[a+b[2]]

mult235711a=mult235711.copy()

for a in mult235711:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            mult235711a.remove(a)

            break



mult23571113=[]

for a in mult235711a:

    for b in mult13b:

        if a[5:7]!=b[0:2]:
            continue

        else:
            mult23571113=mult23571113+[a+b[2]]

mult23571113a=mult23571113.copy()

for a in mult23571113:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            mult23571113a.remove(a)

            break



multx=[]

print(multx)
print(mult17b)

for a in mult23571113a:

    for b in mult17b:

        if a[6:8]!=b[0:2]:
            continue
        else:
            multx=multx+[a+b[2]]

        
multxa=multx.copy()

for a in multx:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            multxa.remove(a)

            break
print(multxa)

jokelist=[]
for q in range(0,10):

    boze=str(q)

    for p in multxa:

        bozo=str(q)+p
        jokelist=jokelist+[bozo]

jokelista=jokelist.copy()
for a in jokelist:
    jill=a
    for b in range(0,10):
        if jill.count(str(b))>1:
            jokelista.remove(a)

print(jokelista)

duck=0
for g in jokelista:

    duck=duck+int(g)

print(duck)

    


    
