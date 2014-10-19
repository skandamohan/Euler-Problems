'''https://projecteuler.net/problem=5'''
'''Please see the README document for details'''

import math

def run(upper_bound):
	primes = find_primes_under(upper_bound) 
	divisors = []
	result = 1
	for counter in primes:
		highest_power = 1
		while(math.pow(counter,highest_power+1)<upper_bound):
			highest_power = highest_power+1
		divisors.append(int(math.pow(counter,highest_power)))
	print divisors
	for counter in divisors:
		result = result * counter
	print "Lowest common multiple for all values under "+str(upper_bound)+" is "+str(result)


def find_primes_under(limit):
	prime_list = []
	if limit < 2:
		print "Number under 2. No prime numbers available."
		return prime_list
	for counter in range (2, limit+1):
		if not prime_list:
			prime_list.append(counter)
		else:
			if not any(counter%x == 0 for x in prime_list):
				prime_list.append(counter)
	print prime_list
	return prime_list

if __name__  == "__main__":
        print "https://projecteuler.net/problem=5"
