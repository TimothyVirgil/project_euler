'''Solution to Project Euler Problem 23
Code by Timothy Virgil Payne Jr.
Started: 4/30/2020
Completed: 4/30/2020 
I make a list of abundant numbers up to 28123.
Then I make a set of the sums so there are no repeats.
Then I subtract this set from the set of integers from 1 to 28123.
Then I sum this.'''
def abund_check(a):

	curr_fact_count = 1
	
	for b in range(2, int(a ** 0.5) + 1):
		if a % b == 0:
			curr_fact_count += b
			curr_fact_count += (a//b)

	if int(a**0.5)**2 == a:
		curr_fact_count -= int(a ** 0.5)

	if curr_fact_count > a:
		return True

	else:
		return False

def not_abun_sum():

    abund_list = [x for x in range(2,28124) if abund_check(x)]
    
    abun_sum_set = set()
    non_sum_set = set()
    num_set = {x for x in range(28124)}
    
    for a in range(0,len(abund_list)):
        for b in range(a,len(abund_list)):
            abun_sum_set.add(abund_list[a] + abund_list[b])
    
    else:
        non_sum_set = num_set - abun_sum_set
        print(sum(non_sum_set))
        
if __name__ == '__main__':
    
    not_abun_sum()
    
