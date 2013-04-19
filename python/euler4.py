###############################################################################
# Euler 4
# http://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

import time

# Using Python "extended slice" syntax. It works by doing [begin:end:step]
# By leaving begin and end off and specifying a step of -1, it reverses a string.
#
# Example: 
# x = range(10)
# print x[::2]
# [0, 2, 4, 6, 8]
def is_palindrome(n):
	return str(n)[::-1] == str(n)


def get_largest_3_digit_palindrome():
	palindrome = 0
	for i in xrange(100, 1000):
		for j in xrange(i, 1000):
			product = i * j
			if is_palindrome(product):
				if product > palindrome: palindrome = product

	return palindrome

start = time.time()
result = get_largest_3_digit_palindrome()
elapsed = (time.time() - start)
print "result %s returned after %s seconds (1 iteration)." % (result, elapsed)



def get_largest_3_digit_palindrome_optimized():
	palindrome = 0
	for i in xrange(999, 99, -1):
		for j in xrange(i, 99, -1):
			product = i * j

			# Optimization: Since we're decreasing, nothing else in the row can be bigger
			if (product < palindrome): break

			if is_palindrome(product):
				if product > palindrome: palindrome = product

	return palindrome

start = time.time()
result = get_largest_3_digit_palindrome_optimized()
elapsed = (time.time() - start)
print "result %s returned after %s seconds (1 iteration)." % (result, elapsed)