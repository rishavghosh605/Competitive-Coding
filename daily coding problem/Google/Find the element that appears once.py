'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

'''

INT_SIZE = 32
  
def getSingles(arr, n) : 
      
    # Initialize result 
    result = 0
      
    # Iterate through every bit 
    for i in range(0, INT_SIZE) : 
          
        # Find sum of set bits  
        # at ith position in all  
        # array elements 
        sm = 0
        x = (1 << i) 
        for j in range(0, n) : 
            if (arr[j] & x) : 
                sm = sm + 1
                  
        # The bits with sum not  
        # multiple of 3, are the 
        # bits of element with  
        # single occurrence. 
        if (sm % 3) : 
            result = result | x 
      
    return result 
# Time and Space: O(N) and O(1)
def getSingle(arr, n): 
	ones = 0
	twos = 0
	
	for i in range(n): 
		# one & arr[i]" gives the bits that 
		# are there in both 'ones' and new 
		# element from arr[]. We add these 
		# bits to 'twos' using bitwise OR 
		twos = twos | (ones & arr[i]) 
		
		# one & arr[i]" gives the bits that 
		# are there in both 'ones' and new 
		# element from arr[]. We add these 
		# bits to 'twos' using bitwise OR 
		ones = ones ^ arr[i] 
		
		# The common bits are those bits 
		# which appear third time. So these 
		# bits should not be there in both 
		# 'ones' and 'twos'. common_bit_mask 
		# contains all these bits as 0, so 
		# that the bits can be removed from 
		# 'ones' and 'twos' 
		common_bit_mask = ~(ones & twos) 
		
		# Remove common bits (the bits that 
		# appear third time) from 'ones' 
		ones &= common_bit_mask 
		
		# Remove common bits (the bits that 
		# appear third time) from 'twos' 
		twos &= common_bit_mask 
	return ones 

# Time and Space: O(N) and O(N)
def find_integer(n):
    not_duplicate=set(n)
    # Stores the number of occurrence of all except one integer
    occurrence=int(input("Enter the occurrence: "))
    # Stores the sum of integers
    S=sum(not_duplicate)
    result= (3*S-(sum(n)))//2
    print(result)
    
if __name__=="__main__":

    # n stores the list of integers by splitting the string and mapping each delimited part of a string as an integer into the list
    n=list(map(int,input("Enter the list of integers: ").split(' ')))
    find_integer(n)
    print("The element with single occurrence is ", 
		getSingle(n,len(n))) 
    print("The element with single occurrence is ", 
		getSingles(n,len(n))) 
	



