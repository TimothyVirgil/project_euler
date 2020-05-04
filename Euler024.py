'''Solution to Project Euler Problem 24
Code by Timothy Virgil Payne Jr.
Started: 5/4/2020
Completed:
I'll use itertools to generate the lexicographic permutations and a counter to
return the result when we're on the 1_000_000th permutation.
'''
from itertools import permutations

def lexo_perm():
    
    count_perm = enumerate(permutations('0123456789'))
    
    for a in count_perm:  
        
        if a[0] == 999_999:
            ans = ''
            
            for x in a[1]:
                ans += x
                
            else:
                print(ans)
              
if __name__ == '__main__':
    
    lexo_perm()