import sys

def individual_factor_distribution(upperbound):
	prime_factors = [2]
	prime_factor_count = [1]
	for counter in range (3, upperbound+1):
		prime_flag = True
		for inner_counter in prime_factors:
			if counter%inner_counter == 0:
				prime_flag = False
				prime_factor_count[prime_factors.index(inner_counter)] = prime_factor_count[prime_factors.index(inner_counter)]+1
		if prime_flag == True:		
			prime_factors.append(counter)
			prime_factor_count.append(1)
	print "Counter:"+str(upperbound)+" Factors:"+str(prime_factors) + " Distribution:" + str(prime_factor_count)

def run(upperbound):
	for outer_counter in range (2, upperbound+1):
		individual_factor_distribution(outer_counter)

if __name__  == "__main__":
        run(int(str(sys.argv[1])))
