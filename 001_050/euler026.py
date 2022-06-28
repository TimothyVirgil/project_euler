'''Solution to Project Euler Problem 26
Code by Timothy Virgil Payne Jr.
Started: 5/7/2020
Completed: 5/8/2020
'''
def longest_cycle():

    curr_max = (0,0)

    for d in range(2,1000):    
    
        rList=[]       
    
        for b in range(1,d): #cycle can only be d-1 long
    
            if 10**b%d==0:
                break
    
            elif 10**b%d in rList:                
                if len(rList) > curr_max[1]:
                        curr_max = (d,len(rList))                
                break
            
            else:
                rList += [10**b%d]
    
        else:
            curr_max = (d,len(rList))
    
    print(curr_max)
        
if __name__ == '__main__':
    
    longest_cycle()