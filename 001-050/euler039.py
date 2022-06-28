'''Solution to Project Euler Problem 39
Code by Timothy Virgil Payne Jr.
Started: 8/31/21
Completed: 8/31/21
'''

count_dict={}

for d in range(1,499):

    for e in range(1,499):
        c=(d**2+e**2)**(0.5)

        if c.is_integer():            

            if int(c)+d+e>1000:
                break

            elif int(c)+d+e not in count_dict.keys():                
                count_dict[int(c)+d+e]=1

            else:
                count_dict[int(c)+d+e]+=1


val_list=list(count_dict.values())
key_list=list(count_dict.keys())
print(key_list[val_list.index(max(val_list))])

