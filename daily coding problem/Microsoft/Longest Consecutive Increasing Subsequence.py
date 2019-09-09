'''
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
def findConsecutiveCount(l):

    s=set(l)
    longest=0
    for i in s:
        if i-1 not in s:
            counter=0
            ele=i
            while ele in s:
                counter+=1
                ele+=1
            longest=max(counter,longest)
    return longest

if __name__=="__main__":

    l=list(map(int,input("Enter the integers: ").split(' ')))
    result=findConsecutiveCount(l)
    print("The length of the longest consecutive increasing susequence is: ",result)
