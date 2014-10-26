'''https://projecteuler.net/problem=6'''
'''Please see the README document for details'''

import math
import operator

def run(big_number, number_of_digits):
        big_array = put_digits_of_number_into_array(big_number)
	if len(big_array)-1 < number_of_digits:
		print "Your number of digits is bigger than the BIG number. Please check your arguments"
	start_index = 0
	end_index = len(big_array)
	result = reduce(operator.mul, big_array[:number_of_digits])
	for counter in range(number_of_digits, end_index, 1):
		if big_array[counter - number_of_digits] != 0:
			comparator = reduce(operator.mul, big_array[counter-number_of_digits:counter])
			if(result < comparator):
				#print "Before"+str(result)
				result = comparator
				#print "After "+str(result) 
	print "The largest mutliple is "+str(result)
	return result
	
def put_digits_of_number_into_array(big_number):
	result = []
	while big_number > 0:
		result.insert(0, big_number%10)
		big_number = big_number/10	
	return result

if __name__  == "__main__":
        print "https://projecteuler.net/problem=9"
                                                       
