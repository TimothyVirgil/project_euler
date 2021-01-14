#Project Euler Problem 24: Lexicographic permutations

# A permutation is an ordered arrangement of objects.

#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically,
#we call it lexicographic order.
#The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the
#digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


#1st, we need to generate the list, then call the millionth item.

#I could probaby generate the list then use the sort function.


#But how to generate the list? For loop? Create strings first?

#Let's do some tests


num='0123456789'

quack=''




for a in range(0,10):

    print(quack)

    quack=''

for q in range(0,10):

    quack = quack+num[a]

    for b in range(0,10):
        
        if len(quack)==10:
            break

        if num[b] not in quack:

            quack=quack+num[b]

        for c in range(0,10):

            if len(quack)==10:
                break

            if num[c] not in quack:

                quack=quack+num[c]

            for d in range(0,10):

                if len(quack)==10:
                    break

                if num[d] not in quack:

                    quack=quack+num[d]

                for e in range(0,10):

                    if len(quack)==10:
                        break

                    if num[e] not in quack:

                        quack=quack+num[e]

                    for f in range(0,10):

                        if len(quack)==10:

                            break

                        if num[f] not in quack:

                            quack=quack+num[f]


                        for g in range(0,10):

                            if len(quack)==10: break

                            if num[g] not in quack:

                                quack = quack+num[g]

                            for h in range(0,10):

                                if len(quack)==10:

                                            break



                                if num[h] not in quack:

                                    quack=quack+num[h]


                                for i in range(0,10):
                                    
                                    if len(quack)==10:

                                            break



                                    if num[i] not in quack:

                                        quack=quack+num[i]

                                    for j in range(0,10):

                                        if len(quack)==10:

                                            break



                                        if num[j] not in quack:

                                            quack=quack+num[j]

                                       



        
