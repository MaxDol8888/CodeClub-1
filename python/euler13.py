###############################################################################
# Euler 13
# http://projecteuler.net/problem=13
#
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#
# See text file euler13.txt for data.
###############################################################################

import time

def calculate_sum(filename):
	
	total = 0

	for line in open(filename).readlines():
		total += int(line)
	
	return total

start = time.time()
for i in range(1000): result = str(calculate_sum("euler13.txt"))[:10]
elapsed = (time.time() - start)
print ("result %s returned after %s seconds (1000 iterations)." % (result, elapsed))
#result 5537376230 returned after 0.19501090049743652 seconds (1000 iterations).



def calculate_sum_using_array(filename):
	
	numbers = open(filename).readlines()

	numbers = []
	for line in open(filename).readlines():
		numbers.append(int(line))
	
	return sum(numbers)

start = time.time()
for i in range(1000): result = str(calculate_sum_using_array("euler13.txt"))[:10]
elapsed = (time.time() - start)
print ("result %s returned after %s seconds (1000 iterations)." % (result, elapsed))
#result 5537376230 returned after 0.33101892471313477 seconds (1000 iterations).



def calculate_sum_using_lambda(filename):
	
	return sum(map(lambda x: int(x), open(filename).readlines()))

start = time.time()
for i in range(1000): result = str(calculate_sum_using_lambda("euler13.txt"))[:10]
elapsed = (time.time() - start)
print ("result %s returned after %s seconds (1000 iterations)." % (result, elapsed))
#result 5537376230 returned after 0.21001219749450684 seconds (1000 iterations).