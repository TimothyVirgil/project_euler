#Euler Project Problem 20

import math

q=math.factorial(100)

digitSum=0

for a in range(0,len(str(q))):

    b = int(str(q)[a])

    digitSum=digitSum + b


print(digitSum)
