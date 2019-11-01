'''Solution to Project Euler Problem 22
Code by Timothy Virgil Payne Jr.
Started: 10/21/19 8:30 PM
Completed: 10/31/19 8:21 PM '''


import sys

names = open("p022_names.txt", 'r')

names_list = names.read().replace('"','').split(',') #read, replace quotes, split into list

names_list.sort()

#Ord of capital A is 65, so if I subtract 64, I should get the letter scores

tot_sum = 0

for x in names_list:
    
    name_score = 0
    
    for char in x:
        
        name_score += ord(char)-64
        
    name_score *= (names_list.index(x)+1)
    
    tot_sum += name_score
    
    
print(f'The total sum of all the name scores is {tot_sum}.\n')

wait = input("Press enter to exit.")

sys.exit()
