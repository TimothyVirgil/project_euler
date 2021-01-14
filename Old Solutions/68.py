# Project Euler 68

#code produces list of 4 possibilities. I found the answer by analyzing those 4 possibilities.

avail = [1,2,3,4,5,6,7,8,9]

five_gon = [10]

poss_sums = list(range(13,21))

poss_combs = []

for a in poss_sums: # iterate through possible sums

    for b in range(1,10): # iterate through 1-9

        avail_1 = avail.copy() # copy availables

        five_gon = [10]

        five_gon += [b] # add the lowest number 

        avail_1.remove(b) # remove from available

        if (a - 10 - b) in avail_1: # check to see if difference is availabe

            c = (a - 10 - b)

            five_gon += [c] # add number to third slot

            avail_1.remove(c) # remove new number from avail list            

        else:

            continue

        for x in range(0,len(avail_1)): # on to number 4, iterate through available numbers
            
            five_gon1 = five_gon.copy() # new poss list

            avail_2 = avail_1.copy() # new available list

            d = avail_2[x] # current number
           
            five_gon1 += [d] # add 4th number

            avail_2.remove(d) # remove 4th number

            if ( a - c - d ) in avail_2:

                e = (a - c - d)

                five_gon1 += [e]

                avail_2.remove(e)

            else:

                continue

            for y in range(0,len(avail_2)): # on to number 6 iterate through availables

                five_gon2 = five_gon1.copy()

                avail_3 = avail_2.copy()

                f = avail_3[y] #current number

                five_gon2 += [f]

                avail_3.remove(f)

                if ( a - f - e) in avail_3:

                    g = (a - f - e)

                    five_gon2 += [g]

                    avail_3.remove(g)

                else:

                    continue


                for q in range(0,len(avail_3)): # on to number 8 iterate through

                    five_gon3 = five_gon2.copy()

                    avail_4 = avail_3.copy()

                    h = avail_4[q]

                    five_gon3 += [h]

                    avail_4.remove(h)

                    if (a - h - g) in avail_4:

                        i = ( a - h - g)

                        five_gon3 += [i]

                        avail_4.remove(i)

                        if (avail_4[0] + i + b) == a:

                            five_gon3 += [avail_4[0]]

                            poss_combs += [five_gon3]

                            continue
                            



print(poss_combs)


            
    
