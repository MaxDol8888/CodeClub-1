###############################################################################
# Euler 3
# http://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
###############################################################################



import time

# Iterate through a range up to 1 more than the square root of the number we're
# trying to determine is prime - denoted by the variable n.  We can do this
# because if n is not prime, then it can be factored into two factors, a & b...
# and if both a & b were greater than the square root, then a * b would be
# greater than n.  This means at least one of those factors must be less or
# equal to the square root of n, so to check if n is prime, we only need to
# test for factors less than or equal to the square root.
#
def is_prime(n):
	for cur in xrange(2, int(n ** .5) +1):
		if n % cur == 0: return False

	return True

 
# Starting with the 2 variablees cur & highest, where cur is equal to 1 and
# highest is equal to n (i.e. the fist 2 factors of a number - 1 and itself),
# iterating while the cur value is less than the highest factor.  If n is
# divisible by cur, then cur is a factor, along with the quotient of n / cur.
# The quotient of n / cur is then set to the highest factor since we won't
# have any factors larger than it given we began the loop dividing by 1 and
# are incrementing by 1 from there.
# 
def get_factors(n):
	cur, highest = 1, n
	while cur < highest:
		if n % cur == 0:
			yield cur
			yield n / cur
			highest = n / cur

		cur += 1


# Iterate throgh the list of factors returned by get_prime_factors(), and test
# if each of them is prime.  If so, return the value.  This will provide us with
# a list of prime factors.
#
def get_prime_factors(n):
	for factor in get_factors(n):
	    if is_prime(factor):
			yield factor

start = time.time()
for i in xrange(10): maxprime = max(get_prime_factors(600851475143))
elapsed = (time.time() - start)
print "result %s returned after %s seconds (10 iterations)." % (maxprime, elapsed)



# A quicker way to determine prime factors
#
# For the range from 2 up to the square root + 1 of n, generate numbers for
# which n % x == 0 is true. The call to next gets the first such number. If
# there are no valid numbers left in the expression, next returns n.  We then
# recursively call the function again but this time passing in n divided by
# the prime factor that was just returned.
#
# get_prime_factors_using_recursion(100)
# return [2] + get_prime_factors_using_recursion(100 / 2)
# return [2] + [2] + get_prime_factors_using_recursion(50 / 2)
# return [2] + [2] + [5] + get_prime_factors_using_recursion(25 / 5)
# return [2] + [2] + [5] + [5] + get_prime_factors_using_recursion(5 / 5)
# return [2] + [2] + [5] + [5] + []
# [2, 2, 5, 5]
#
def get_prime_factors_using_recursion(n):
    if n <= 1: return []
    prime = next((x for x in xrange(2, int(n ** .5)+1) if n%x == 0), n)
    return [prime] + get_prime_factors_using_recursion(n / prime)

start = time.time()
for i in xrange(1000): maxprime = max(get_prime_factors_using_recursion(600851475143))
elapsed = (time.time() - start)
print "result %s returned after %s seconds (1000 iterations)." % (maxprime, elapsed)


# Same as above, but using a generator.  Performance is the same.
def get_prime_factors_using_generator(n):
    if n <= 1: return
    prime = next((x for x in xrange(2, int(n**.5)+1) if n%x == 0), n)
    yield prime
    
    for p in get_prime_factors_using_generator(n / prime):
    	yield p

start = time.time()
for i in xrange(1000): maxprime = max(get_prime_factors_using_generator(600851475143))
elapsed = (time.time() - start)
print "result %s returned after %s seconds (1000 iterations)." % (maxprime, elapsed)
