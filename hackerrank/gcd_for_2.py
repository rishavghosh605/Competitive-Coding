#GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them.
#A simple solution is to find all prime factors of both numbers, then find intersection of all factors present in both numbers. Finally return product of elements in the intersection.

#An efficient solution is to use Euclidean algorithm which is the main algorithm used for this purpose. The idea is, GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number.

#filter_none

# Recursive function to return gcd of a and b 
def gcd(a,b): 
      
    # Everything divides 0  
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
  
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b):
        print(a,b,"1")
        return gcd(a-b, b)
    print(a,b,"2")
    return gcd(a, b-a) 
  
# Driver program to test above function 
a = 16
b = 96
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 

    
  

#Note: A recursive function is taken thus numbers with a huge difference cannot be taken (40000000,1)
#Now what happens is that this algorithm is for 2 numbers but we need a slighter different method for gcd of n numbers
