#Euler Project Problem 40

q=''

for a in range(1,1000000):

    q=q+str(a)



print(int(q[0])*int(q[9])*int(q[99])*int(q[999])*int(q[9999])*int(q[99999])*int(q[999999]))
