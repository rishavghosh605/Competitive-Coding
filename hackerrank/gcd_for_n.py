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
        return gcd(a-b, b)
    return gcd(a, b-a) 
  
# Driver program to test above function 
l=[20,30,12]
result=l[0]
for i in range(1,len(l)):
    result=gcd(result,l[i])
print("result= ",result)

#Note: This algorithm is for gcd of numnbers but we get limited due to
# recursion thus we can use a loop if we test cases which need more number of recursions that is more tham 995 repetitions of the same line.
    
  

