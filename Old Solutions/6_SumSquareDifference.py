clown = 0
lion = 0

for bozo in range(1,101):
    clown = clown + bozo**2


for strongman in range(1,101):
    lion = lion + strongman


lion = lion**2

answer = lion - clown

print('The answer is ' + str(answer) + '.')
