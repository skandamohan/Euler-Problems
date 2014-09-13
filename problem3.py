'''https://projecteuler.net/problem=3'''
'''Please see the README document for details'''

def run(upper_bound):
	prime_factor_list = []
	counter = 2
	while(counter < upper_bound):
		prime_factor_list_counter = 0
		for prime_factor in prime_factor_list:
			if(counter%prime_factor == 0):
				break
			else:
				prime_factor_list_counter = prime_factor_list_counter + 1

		if(prime_factor_list_counter == len(prime_factor_list)):
			prime_factor_list.append(counter)
			# Warning: HUGE output for large upper_bounds
			print str(prime_factor_list[-1])+", ",

		counter = counter+1;

	print "Highest Prime lower that "+str(upper_bound)+" is "+str(prime_factor_list[-1])

if __name__  == "__main__":
        print "https://projecteuler.net/problem=2"

