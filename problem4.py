'''https://projecteuler.net/problem=4'''
'''Please see the README document for details'''

import math

def run(power):
	counter = int(math.pow(10,power+power))-1
        lower_bound = int(math.pow(10,power+power-1))
	lower_lower_bound = int(math.pow(10,power-1))
	lower_upper_bound = int(math.pow(10,power))

	palindromes = []

	while(counter>lower_bound):
		if(check_palindrome(counter)):
			palindromes.append(counter)
		counter = counter - 1
	#print "Palindromes with "+str(power*2)+" digits are "+str(palindromes)
	for num in palindromes:
	        counter = int(math.pow(10,power))-1
		factors = []
		while(counter>lower_lower_bound):
			if(num%counter==0 and num/counter > lower_lower_bound-1 and num/counter < lower_upper_bound):
				factors.append(counter)
				if(len(factors) > 1):
					print "Highest palindrome with "+str(power*2) +" digits that have two "+str(power)+" digit factors is: "+str(factors[0]*factors[1]) + " with factors "+str(factors[0])+" and "+str(factors[1])
					return factors[0]*factors[1]
			counter = counter -1
	return -1

def check_palindrome(number):
	checker = []
	while(number>0):
		reminder = int(number%10)
		checker.append(reminder)
		number = number/10
	for inc in range(len(checker)):
		if(checker[inc]!=checker[len(checker)-inc-1]):
			return False
	return True

if __name__  == "__main__":
        print "https://projecteuler.net/problem=4"
