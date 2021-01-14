

for clown in range(1,900):
	for bozo in range(1,900):
		if bozo>=clown:
			break
		for joker in range(1,900):
			if joker>=bozo:
				break
			elif (joker**2+bozo**2)==clown**2:
				if joker+bozo+clown==1000:
					print('The numbers are: ' + str(joker) + ', ' + str(bozo) + ', and' + str(clown) + '.')
					print('The product is: ' + str(joker*bozo*clown) + '.')
				
