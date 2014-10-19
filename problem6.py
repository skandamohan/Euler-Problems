'''https://projecteuler.net/problem=6'''
'''Please see the README document for details'''

import math

def run(limit):
	result = 0
	print "Way #1"
	for outer_counter in range(1, limit+1, 1):
		for inner_counter in range(outer_counter+1,limit+1,1):
			result = result + 2*outer_counter*inner_counter
	print "Difference between (1^2+2^2+ ... +"+str(limit)+"^2) and (1+2+3 ... +"+str(limit)+")^2 is "+str(result)
	print "Way #2"
	sum_square = 0
	square_sum = 0
	for counter in range(1, limit+1, 1):
		sum_square = sum_square + math.pow((counter),2)
		square_sum = square_sum + counter
	result = math.pow(square_sum,2) - sum_square
	print str(math.pow(square_sum,2)) +"-"+ str(sum_square) +" is "+str(result)
        print "Difference between (1^2+2^2+ ... +"+str(limit)+"^2) and (1+2+3 ... +"+str(limit)+")^2 is "+str(result)


if __name__  == "__main__":
        print "https://projecteuler.net/problem=6"
                                                       
