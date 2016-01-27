'''https://projecteuler.net/problem=39'''
'''Please see the README document for details'''

import math
import operator

def run(upto):
	pythogorean_map = {}
	most_pythogorean = 0;
#Start from perimeter/2 as no side of a triangle can be more than total perimeter/2
	for i in range (upto/2,0,-1):
#Start from the above value to not double count same value (49,50) vs (50,49)
		for j in range (i,0,-1):
			#print str(i) + " " + str(j) + " ",
			hypotenuse = get_hypotenuse(i,j)
#Only if the hypotenuse is an integer value add it to the map
			if(hypotenuse.is_integer() and ((hypotenuse+i+j)<=upto)):
	                        #print "hypotenuse "+ str(hypotenuse),
				if((hypotenuse+i+j) in pythogorean_map):
					pythogorean_map[hypotenuse+i+j] = pythogorean_map[hypotenuse+i+j]+1
					if(pythogorean_map[hypotenuse+i+j] > most_pythogorean):
						most_pythogorean = pythogorean_map[hypotenuse+i+j];
				else:
					pythogorean_map[hypotenuse+i+j] = 1
					if(1 > most_pythogorean):
                                                most_pythogorean = 1
	print pythogorean_map
	perimeter = 0
	for key, value in pythogorean_map.iteritems():
		if(value == most_pythogorean):
			perimeter = key
	print "Most number of pythogorean triplets for a perimeter under " + str(upto) + " is " + str(perimeter)

def get_hypotenuse(a,b):
	return math.sqrt(math.pow(a,2)+math.pow(b,2))

def check_square_law(a,b,c):
	if(a>c):
		a,c = c,a
	if(b>c):
		b,c = c,b
	return math.pow(c,2) == math.pow(a,2) + math.pow(b,2)
		
	

if __name__  == "__main__":
        print "https://projecteuler.net/problem=39"
