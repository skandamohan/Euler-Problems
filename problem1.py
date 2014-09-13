'''https://projecteuler.net/problemi=1'''
'''Please see the README document for details'''

def run(factor_list, lower_bound, upper_bound):
	solution = 0
	print "Sum of all mulitples of "+', '.join(str(factor) for factor in factor_list)+" between "+str(lower_bound)+" and "+str(upper_bound)
	for counter in range(lower_bound, upper_bound):
		for factor in factor_list:
			if counter%factor == 0:
				solution = solution + counter
				print (str(counter)+" "), 
				break
	print "= "+str(solution)

if __name__  == "__main__":
	print "https://projecteuler.net/problem=1"
