#This is a program that does 2 things:
# 1. Determines if a number is prime
# 2. If not, lists all the prime factors.

def circus():
    global number
    for bozo in range(2,number+1):

            if bozo==number:
                print(str(number) + ' is a prime factor.')

            elif number%bozo==0:
                break
    
print('This program will determine if your number is prime. If it is composite, the program will list the prime factors.')
print("Please enter your number. I'm new to programming, so keep it 8 digits or less, please.")

clown = 2000001

while clown >=100000000:
      print('That number is larger than 8 digits. Please, it must be 8 digits or lower. Try again.')
      clown = int(input())
            

for number in range(2,clown):
    if clown%number==0:
        circus()
        
for strongman in range(2,clown+1):

        if strongman == clown:
            print('Your number is prime. ' + str(clown) + ' is a prime number.')
            
        elif clown%strongman == 0:
            print('Your number is composite. ' + str(clown) + ' is a composite number.')
            break
                
    
            
