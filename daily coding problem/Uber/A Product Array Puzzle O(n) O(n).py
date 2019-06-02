# Python3 program for A Product Array Puzzle 
def productArray(arr, n): 

	i, temp = 1, 1

	# Allocate memory for the product array 
	prod = [1 for i in range(n)] 

	# Initialize the product array as 1 

	# In this loop, temp variable contains product of 
	# elements on left side excluding arr[i] 
	for i in range(n): 
		prod[i] = temp 
		temp *= arr[i] 

	# Initialize temp to 1 for product on right side 
	temp = 1

	# In this loop, temp variable contains product of 
	# elements on right side excluding arr[i] 
	for i in range(n - 1, -1, -1): 
		prod[i] *= temp 
		temp *= arr[i] 

	# Print the constructed prod array 
	for i in range(n): 
		print(prod[i], end = " ") 

	return

# Driver Code 
arr = [10, 3, 5, 6, 2] 
n = len(arr) 
print("The product array is: n") 
productArray(arr, n) 

'''Output :
The product array is : 
180 600 360 300 900 
Time Complexity: O(n)
Space Complexity: O(n)
Auxiliary Space: O(1)'''

