#Projecteuler.net problem 12: Highly divisible triangular number


triangleNumber = 0
triangleFactor = []
import math

for q in range(1,100000000000):

    if len(triangleFactor)>500:
                print('The first triangle with over 500 divisors is ' + \
                str(triangleNumber) + '.')
                exit()
    
    triangleFactor = []
        
    triangleNumber = triangleNumber + q

    if triangleNumber%2==0:

        for b in range(1,round(math.sqrt(triangleNumber))+1):

            if b not in triangleFactor:

                if math.sqrt(triangleNumber)==b:
                    triangleFactor = triangleFactor + [b]
                    break

       
                elif triangleNumber%b==0:
                    triangleFactor = triangleFactor + [b] + [triangleNumber/b]

            
        

    
