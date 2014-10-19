'''Test cases for problems for https://projecteuler.net/problems'''
'''Please see the README document for details'''

import problem1
import problem2
import problem3
import problem4
import problem5
import problem6


underline = '\033[4m'
end = '\033[0m'

print "https://projecteuler.net/"
print underline+"Problem 1"+end
problem1.run([3,5],0,10)
print underline+"Problem 2"+end
problem2.run(100000)
print underline+"Problem 3"+end
problem3.run(6843)
print underline+"Problem 4"+end
problem4.run(2)
print underline+"Problem 5"+end
problem5.run(10)
print underline+"Problem 6"+end
problem6.run(10)
print underline+"Problem 7"+end

