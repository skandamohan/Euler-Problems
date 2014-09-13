'''https://projecteuler.net/problem=2'''
'''Please see the README document for details'''

def run(upper_bound):
	print "Sum of even Fibonacci Numbers between 0 and "+str(upper_bound)
	solution = 0
	fib_counter1 = 1
	fib_counter2 = 1
	counter_flag = True # false for counter1, true for counter2
	while (fib_counter1 < upper_bound and fib_counter2 < upper_bound):
		print("Fib1 = "+str(fib_counter1)+", Fib2 = "+str(fib_counter2) + ", Sum = "+str(fib_counter1+fib_counter2)), 
		if((fib_counter1+fib_counter2)%2 ==0):
			solution = solution + fib_counter1 + fib_counter2
			print("Solution = "+str(solution)+", "),
		if counter_flag:
			fib_counter2 = fib_counter1 + fib_counter2
		else:
			fib_counter1 = fib_counter1 + fib_counter2
		counter_flag = not counter_flag
		print ""
	print solution

if __name__  == "__main__":
        print "https://projecteuler.net/problem=2"
