sumPrimes = 17

for bozo in range(11,2000000,2):
        
        for number in range(3,round(bozo/2+1),2):
                if int(str(bozo)[-1])==5:
                        break
        
                elif number==round(bozo/2+1):
                    sumPrimes = sumPrimes + bozo
                elif bozo%number==0:
                        break

print('The sum of all primes below two million is: ' + str(sumPrimes) + '.')
            
            
