'''https://projecteuler.net/problem=5'''
'''Please see the README document for details'''

def run(upper_bound):
	upper_bound = upper_bound+1
	result = 1
	highest_common_multiples = []
	for counter in range (2,upper_bound,1):
		for inner_counter in range(2,counter):
			print "counter = "+str(counter)+" inner_counter = "+str(inner_counter)
			if(counter%inner_counter == 0):
				if inner_counter in highest_common_multiples:
					highest_common_multiples.remove(inner_counter)
		if counter not in highest_common_multiples:
			highest_common_multiples.append(counter)
	print highest_common_multiples
	for counter in highest_common_multiples:
		result = result * counter
		highest_common_multiples.remove(counter)
		for inner_counter in highest_common_multiples:
			if(result%inner_counter == 0):
				highest_common_multiples.remove(inner_counter)
	for counter in highest_common_multiples:
		result = result*counter
	#print "Initial result: "+ str(result)
	#for counter in highest_common_multiples:
	#	while((result/counter)%counter == 0):
	#		result = result/counter
	print "Lowest common multiple between all the numbers below "+str(upper_bound)+" is "+str(result)
	print "https://projecteuler.net/problem=5 - END ----------------"

if __name__  == "__main__":
        print "https://projecteuler.net/problem=5"
