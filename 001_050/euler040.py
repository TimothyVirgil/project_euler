'''Solution to Project Euler Problem 40
Code by Timothy Virgil Payne Jr.
Started: 9/1/21
Completed: 9/1/21
'''

num = ''

for a in range(1, 185186):
    num = num+str(a)

print(int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])
      * int(num[99999])*int(num[999999]))
