for clown in range(0,35):
	for bozo in range(0,35):
		if bozo>=clown:
			break
		for joker in range(0,35):
			if joker>=bozo:
				break
			elif (joker**2+bozo**2)==clown**2:
				if joker+bozo+clown==1000:
                                        print('The numbers are: ' + str(joker) + ', ' + str(bozo) + ', and' + str(clown) + '.')
				
