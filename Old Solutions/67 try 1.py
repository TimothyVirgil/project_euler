#Euler 67
#I'm trying to read a file and make a list. Each line
#should be a list inside that list.

## This is a file to read through 100 rows of a triangle file and find the 
## highest possible sum

import os

f = open("c:\\users\\cabba\\Onedrive\\Programs\\Euler Project\\p067_triangle.txt") ## open file

tri_list = []          ##blank list

for line in f: ##iterate through lines

    

    str_line = line.replace(" ", "")  ##remove whitespace
    str_line = str_line.rstrip("\n") ##remove endline character

    
    john = [] ## temporary list for loop

    for a in range(0, len(str_line), 2): ## iterate through line
        bill = int(str_line[a] + str_line[a+1]) ## turn two string digits into integer
        john += [bill] ## add integer to temporary list


    tri_list += [john] ## add list of this line to our master list

prev_list = [tri_list[0][0]+ tri_list[1][0], tri_list[0][0] + tri_list[1][1]]



for a in range(2, len(tri_list)):  ## iterate through our list of triangle rows

    curr_list = [] ## our current list of totals

    curr_list += [ tri_list[a][0] + prev_list[0] ] ## add the left most values to current total list

    for b in range(1, len(prev_list)): ## iterate through current row of triangle, finding the current max

        curr_list += [ max(prev_list[b-1], prev_list[b]) + tri_list[a][b] ]

    curr_list += [ tri_list[a][-1]  + prev_list[-1] ] ## add the right most values

    
    prev_list = curr_list ## refresh current list

    
    

print(max(curr_list)) ## find the highest total

os.system('pause')
