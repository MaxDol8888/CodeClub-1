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
	sum = 0

	for line in open(filename).readlines():
		sum += int(line)
	
	return sum

start = time.time()
for i in range(1000): result = str(calculate_sum("euler13.txt"))[:10]
elapsed = (time.time() - start)
print ("result %s returned after %s seconds (1000 iterations)." % (result, elapsed))
#result 5537376230 returned after 0.19401121139526367 seconds (1000 iterations).