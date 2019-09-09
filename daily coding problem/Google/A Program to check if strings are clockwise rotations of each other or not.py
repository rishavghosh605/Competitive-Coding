"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def isClockwiseRotated(a,b):
    
    if (len(a)!=len(b)):
        return False
    temp=""
    for pos in range(len(b)):
        if a[0]==b[pos]:
            temp=b[pos:]+b[:pos]
        if temp==a:
            return True
    return False
if __name__=="__main__":

    a=input("Enter the string A: ")
    b=input("Enter the string B: ")

    print("The result is: ",isClockwiseRotated(a,b))
