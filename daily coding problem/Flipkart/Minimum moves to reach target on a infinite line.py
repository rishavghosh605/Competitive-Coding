'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Flipkart.

Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.
'''
import math
def findMinJumps(N):
    N=abs(N)
    i=math.ceil((-1.0+math.sqrt(1+8.0*N))/2)
    sum=(i*(i+1))/2
    diff=int(sum-N)
    if(diff%2==0):
        return i
    else:
        if(i%2!=0):
            return i+2
        else:
            return i+1

if __name__=="__main__":

    N=int(input("Enter the integer: "))# using abs because of symmetry
    i=findMinJumps(N)
    print(i)
