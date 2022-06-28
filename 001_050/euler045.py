'''Solution to Project Euler Problem 45
Code by Timothy Virgil Payne Jr.
Started: 1/15/22
Completed: 1/15/22
'''

def pentest(p):
    n = int(((1 + 24*p) ** 0.5 + 1)/6) 
    if n*(3*n-1)/2 == p:
        return True
    else:
        return False

def hextest(h):
    n = int(((1 + 8*h) ** 0.5 +1)/4)    
    if n*(2*n-1) == h:
        return True    
    else:
        return False

def tripletest(a):    
    tri = a*(a + 1)//2    
    if pentest(tri) and hextest(tri):
        return tri    
    else:
        return False

def run_test(start=286):
    x = start    
    while True:    
        curr_tri = tripletest(x)    
        if curr_tri != False:
            print(curr_tri)
            break    
        else:
            x += 1
            continue

if __name__ == '__main__':
	run_test()
