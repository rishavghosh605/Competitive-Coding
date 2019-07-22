"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def findLongestSubsequence(arr):

    length=[1 for i in range(len(arr))]
    for i in range(len(arr)):
        j=0
        for j in range(j,i+1):
            print(arr[j],end=" ")
            if arr[j]<arr[i]:
                if length[j]+1>length[i]:
                    length[i]=length[j]+1
        print("",end='\n')

    print(length)
    result=max(length)
    return result
    

if __name__=="__main__":

    #arr=list(map(int,input("Enter the array: ")))
    arr=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("The longest subsequence is: ",findLongestSubsequence(arr))
