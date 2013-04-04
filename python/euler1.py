###############################################################################
# Euler 1
# http://projecteuler.net/index.php?section=problems&amp;id=1
#
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23. Find the sum of all the multiples
# of 3 or 5 below 1000.
###############################################################################

# Determine multiples of 3 & 5 below a max value via a while loop and add them
# to list.
def multiples_of_3_or_5(end):
	number = 1
	multiples = []
	while number < end :
		if number % 3 == 0 or number % 5 == 0:
			multiples.append(number)
		number = number + 1

	return multiples

total = sum(multiples_of_3_or_5(1000))
print "multiples_of_3_or_5: %d" % total


# Determine multiples of 3 & 5 below a max value using a range generator.
#
# Note: we are using xrange instead of range.  Range actually creates the list
# in memory.  Xrange returns an xrange object instead of a list which yields
# the values without actually storing them all simultaneously.
def multiples_of_3_or_5_using_range(end):
	for number in xrange(end):
		if number % 3 == 0 or number % 5 == 0:
			yield number
			number = number + 1

total = sum(multiples_of_3_or_5_using_range(1000))
print "multiples_of_3_or_5_using_range: %d" % total


# Compute sum of multiples of 3 & 5 below a max value using a range generator.
#
# Note: The difference here is that we're computing the sum as we go.
def sum_multiples_of_3_or_5_using_range(end):
	total = 0
	for number in xrange(end):
		if number % 3 == 0 or number % 5 == 0:
			total = total + number
			number = number + 1
	return total

total = sum_multiples_of_3_or_5_using_range(1000)
print "sum_multiples_of_3_or_5_using_range: %d" % total


# Compute the sum of multiples of 3 & 5 below a max value using two range
# generators, storing the unique values in a set, and computing the sum
# of the values in the set.
def sum_multiples_of_3_or_5_using_two_ranges(end):
	multiples = set([])

	for i in range(3, end, 3):
		multiples.add(i)

	for i in range(5, end, 5):
		multiples.add(i)

	return sum(multiples)

total = sum_multiples_of_3_or_5_using_two_ranges(1000)
print "sum_multiples_of_3_or_5_using_two_ranges: %d" % total


# One liner
def sum_multiples_of_3_or_5_one_liner(end):
	return sum([x for x in range(end) if x % 3== 0 or x % 5== 0])

total = sum_multiples_of_3_or_5_one_liner(1000)
print "sum_multiples_of_3_or_5_one_liner: %d" % total