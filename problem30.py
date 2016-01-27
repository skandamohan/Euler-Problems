'''https://projecteuler.net/problem=30'''
'''Please see the README document for details'''

import math
import operator

def run(power):
	highest_number = find_highest_number_where_number_is_higher_than_sum_of_individual_digits_powered(power)	
	print "Highest number " + str(highest_number),
	numbers_who_are_sums_of_individual_digits_powered = []
	for i in range(2,int(highest_number)+1):
		if(check_if_num_is_sum_of_digits_powered(i, power)):
			numbers_who_are_sums_of_individual_digits_powered.append(i)
	print "All numbers that are sums of " + str(power) + " power their individual digits " + str(numbers_who_are_sums_of_individual_digits_powered)
	return sum(numbers_who_are_sums_of_individual_digits_powered)

##
# This function below was tricky to figure out. Basically, we need to find the number at which we know that adding another 9^power won't make a difference
##
def find_highest_number_where_number_is_higher_than_sum_of_individual_digits_powered(power):
	i = 1
	powered_increase = 0
	decimal_increase = 0
	while(powered_increase >= decimal_increase):
        	powered_increase = math.pow(9,power)*i
        	decimal_increase = math.pow(10,i)-1
	#	print "powered increase " + str(powered_increase) + " decimal increase " + str(decimal_increase)
		i = i+1
	return powered_increase

def check_if_num_is_sum_of_digits_powered(number, power):
	str_ver = str(number)
	sum = 0
	for i in str_ver:
		sum =  sum + math.pow(int(i),power)
	return int(sum) == number	

if __name__  == "__main__":
	print "https://projecteuler.net/problem=30"
