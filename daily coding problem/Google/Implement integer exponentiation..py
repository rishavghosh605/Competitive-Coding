"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y, and where y is non-negative

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

# Naive iterative solution to calculate pow(x, y)
# Time complexity is O(N)
def power1(x,y):
    
    # initialize
    result=1

    for i in range(y):
        result*=x

    return result

# Using divide and conquer:
# We can recursively define the problem as:
# power(x, n) = power(x, n / 2) * power(x, n / 2);        // else n is even*
# power(x, n) = x * power(x, n / 2) * power(x, n / 2);   // if n is odd
# The time complexity of above solution is O(N)


# This is a Naive implementation of the above stated algorithm:
def power2(x,y):

    if y==0:
        return 1

    # using bit manipulation to check if y is odd or not
    if y&1:
        return x*power2(x,y//2)*power2(x,y//2)

    return power2(x,y//2)*power2(x,y//2)

# We can optimize the above solution by using memoization
# We can do this by computinhg the solution of the sub_problem once only rather than calling it twice
# Time complexity is O(LogN)
def power3(x,y):

    if y==0:
        return 1
    result=power3(x,y//2)
    # using bit manipulation to check if y is odd or not,if yes then
    if y&1:
        return x*result*result
    # if not then:
    return result*result

# Using low level programming:
# We use binary operators to calculate pow(x,y)
# Time complexity is O(LogN)
def power4(x,y):

    result=1

    while y:

        if y&1:
            result*=x

        #dividing y by 2
        y=y>>1

        #multiply x by itself
        x=x*x

    return result

if __name__=="__main__":

    print("Enter in the format: pow(x,y)")
    x=int(input("Enter x: "))
    y=int(input("Enter y: "))

    result=power1(x,y)
    print("Product is: ",result)
    
    result=power2(x,y)
    print("Product is: ",result)

    result=power3(x,y)
    print("Product is: ",result)

    result=power4(x,y)
    print("Product is: ",result)

    
