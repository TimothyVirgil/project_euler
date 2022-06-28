'''Solution to Project Euler Problem 30
Code by Timothy Virgil Payne Jr.
Started: 1/25/2021
Completed: 1/25/2021

Testing out some max limits here:

>>> for a in range(1,10):
	print(a**5)	
1
32
243
1024
3125
7776
16807
32768
59049
>>> 59049*5
295245
>>> 59049*6
354294

This means that the max limit will be a six digit number. I can set a loop that goes up to 1,000,000.

Below is a functional, if inelegant, brute force solution
'''

num=0
fifList=[]
fifSum=0

for b in range(2,1000000):
    
    num_str=str(b)

    for q in num_str:

        num=num+int(q)**5

    if num==(b):

        fifList=fifList+[b]

    num=0

    

print(fifList)

for a in fifList:

    fifSum=fifSum+a

print(fifSum) 