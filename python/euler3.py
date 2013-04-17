###############################################################################
# Euler 3
# http://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
###############################################################################



# note: How do we determine the factors of a number?
# note: How do we determine the prime factors of a number?
#
# 1) Determine the factors of a number
# 2) Of the factors of a number, determine while ones are prime
# 3) How do we determine the prime factors of a number?



import time

# Determine if a number is prime
def is_prime(n):
	cur = 2
	while cur < n:
		if n % cur == 0: return False
		cur += 1

	return True

# Determine factors of a number
def get_factors(n):
	cur, lowest = 1, n
	while cur < lowest:
		if n % cur == 0:
			yield cur
			yield n / cur
			lowest = n / cur

		cur += 1

#for factor in get_factors(600851475143):
#	print factor

def get_prime_factors(n):
	for factor in get_factors(600851475143):
	    if is_prime(factor):
			yield factor

print max(get_prime_factors(600851475143))

'''
start = time.time()
for i in xrange(10): maxprime = max(get_prime_factors(600851475143))
elapsed = (time.time() - start)
print "result %s returned after %s seconds (10 iterations)." % (maxprime, elapsed)
'''


def largest_prime_factor(n):
  max = n
  divisor = 2

  while (n >= divisor ** 2):
    if n % divisor == 0:
        max, n = n, n / divisor
    else:
        divisor += 1      

  return max

'''
print largest_prime_factor(600851475143)
start = time.time()
for i in xrange(10): maxprime = largest_prime_factor(600851475143)
elapsed = (time.time() - start)
print "result %s returned after %s seconds (10 iterations)." % (maxprime, elapsed)
'''









'''
def get_primes_using_generator_with_upper(n):
    for i in xrange(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            yield i



def get_prime_factors(n):
	for factor in get_factors(600851475143):
	    if is_prime(factor):
			yield factor


def get_factors(n):
	cur, lowest = 1, n
	while cur < lowest:
		if n % cur == 0:
			yield cur
			yield n / cur
			lowest = n / cur

		cur += 1
'''

def x_using_generator():
	cur = 1
	while True:
		if is_prime(cur): yield cur
		cur += 1

from itertools import takewhile
print max(i for i in takewhile(lambda x: x<21, x_using_generator()))


'''
def get_primes_using_generator():
	prev, cur = 1, 2
	while True:
	    for i in xrange(2, int(math.sqrt(n)+1)):
	        if n % i == 0: 
	            return n;
'''

'''
def get_factors_2(n):
	cur = 1
	x = int(math.sqrt(n))
	while cur <= x:
		if n % cur == 0:
			yield cur
			yield n / cur

		cur += 1

for factor in get_factors_2(20):
	print factor
'''