'''https://projecteuler.net/problem=3'''
'''Please see the README document for details'''

def run(upper_bound):
	if(upper_bound%2 == 0):
		upper_bound = upper_bound-1
	for decrementor in range(upper_bound, 0,-2):
		print str(decrementor)+", ",
		counter = 2
		while(counter < decrementor):
			if(decrementor%counter == 0):
				break
			counter = counter+1
		if(counter == decrementor):	
			print "Highest Prime lower that "+str(upper_bound)+" is "+str(decrementor)
			return
if __name__  == "__main__":
        print "https://projecteuler.net/problem=2"

