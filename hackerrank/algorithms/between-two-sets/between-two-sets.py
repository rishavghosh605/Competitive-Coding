#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#

def find_lcm_gcd(num1, num2,ch): 
    if(num1>num2): 
        num = num1 
        den = num2
    else: 
        num = num2 
        den = num1
    rem = num % den
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den
    gcd = den 
    if(ch==1):
        return gcd
    else:
        lcm = int(int(num1 * num2)/int(gcd))
        return lcm 

def getTotalX(a, b):
   lm = a[0]   
   hcf = b[0]

   for i in range(1, len(a)): 
    lm = find_lcm_gcd(lm, a[i],2) 
   for i in range(1,len(b)): 
    hcf = find_lcm_gcd(hcf,b[i],1)
   l=[]
   for i in range(0,(hcf//lm)):
    if (hcf%(lm*(i+1))==0):
        l.append(lm*(i+1))
   print(lm,hcf)
   return (len(l))

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(total)



#Note: Exception handling:
    # 1> That there can huge numbers big enough to make recursion invalid and looping valid
    # 2> That there can be also only
    #       one integer so if we take the starting element as the lcm then
    #       even if the function which takes two arguments and due to one
    #       element being in the array will be unable to work will still
    #       give the right result as the first element will be stored as lcm
    #       or gcd for that matter.
