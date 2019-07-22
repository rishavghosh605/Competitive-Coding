"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

def findMaxTriplet(l):

    firstMin=0
    secondMin=0
    firstMax=0
    secondMax=0
    thirdMax=0
    
    for i in range(len(l)):

        if l[i] > l[firstMax]:
            firstMax=i
        
        if l[i] < l[firstMin]:
            firstMin=i
            
    secondMin=firstMin+1 if firstMin<len(l)-1 else firstMin-1
    secondMax=firstMax+1 if firstMax<len(l)-1 else firstMax-1

    for i in range(len(l)):

        if l[i] > l[secondMax] and l[i] <= l[firstMax] and i!=firstMax:
            secondMax=i
        
        if l[i] < l[secondMin] and l[i] >= l[firstMin] and i!=firstMin:
            secondMin=i

    for i in range(len(l)):

        if i!=firstMax and i!=secondMax:
            thirdMax=i

    for i in range(len(l)):

        if l[i] > l[thirdMax] and l[i] <= l[secondMax] and i!=firstMax and i != secondMax:
            thirdMax=i

    print(l[firstMin],l[secondMin],", ",l[firstMax],l[secondMax],l[thirdMax])
    max1=l[firstMin]*l[secondMin]*l[firstMax]
    max2=l[firstMax]*l[secondMax]*l[thirdMax]

    return max1 if max1>max2 else max2
        
    
if __name__=="__main__":

    l=list(map(int,input("Enter the list: ").split(' ')))
    #l=[1,2,3,4,5]
    print("The maximum value is: ",findMaxTriplet(l))
