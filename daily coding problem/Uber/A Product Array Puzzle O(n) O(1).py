# Python program for product array puzzle 
# with O(n) time and O(1) space. 


'''Use property of log to multiply large numbers
x = a * b * c * d
log(x) = log(a * b * c * d)
log(x) = log(a) + log(b) + log(c) + log(d)
x = antilog(log(a) + log(b) + log(c) + log(d))'''
import math 

# epsilon value to maintain precision 
EPS = 1e-9

def productPuzzle(a, n): 
	
	# to hold sum of all values 
	sum = 0
	for i in range(n): 
		sum += math.log10(a[i]) 
	
	# output product for each index 
	# antilog to find original product value 
	for i in range(n): 
		print int((EPS + pow(10.00, sum - math.log10(a[i])))), 
	
	return

# Driver code 
a = [10, 3, 5, 6, 2 ] 
n = len(a) 
print "The product array is: "
productPuzzle(a, n) 


'''
Output:
The product array is: 
180 600 360 300 900 

Time complexity : O(n)
Space complexity: O(1)

'''
