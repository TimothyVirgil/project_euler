

for clown in range(20,10000000000000,20):
    for bozo in range(1,22):
        if bozo==21:
            print('The answer is ' + str(clown) + '.')
            break
        elif clown%bozo!=0:
            break
