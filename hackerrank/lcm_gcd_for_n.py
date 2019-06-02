# Python program to find LCM of two numbers 

# Recursive function to return gcd of a and b 
def gcd(a,b): 

	# base case if a and b are equal 
	if (a == b): 
		return a 
	# if a is greater 
	if (a > b): 
		return gcd(a-b, b) 
		
	return gcd(a, b-a) 

# Function to return LCM of two numbers 
def lcm(a,b): 
	return (a*b) / gcd(a,b) 

# Driver program to test above function 
l = [20,30,12]

lm = l[0] 

for i in range(1, len(l)): 
	lm = lcm(lm, l[i]) 
	
print(lm) 


#Note: A recursive function is taken thus numbers with a huge difference cannot be taken (40000000,1)
#Now what happens is that this algorithm is for 2 numbers but we need a slighter different method for lcm of n numbers
