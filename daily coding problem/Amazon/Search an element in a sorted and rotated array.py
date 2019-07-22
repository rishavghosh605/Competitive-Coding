"""
Daily coding problem-description:
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

"""

"""
GeekForGeeks problem description:
An element in a sorted array can be found in O(log n) time via binary search.
But suppose we rotate an ascending order sorted array at some pivot unknown
to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2.
Devise a way to find an element in the rotated array in O(log n) time.
"""
"""
Method of approach: You need to see that the problem asks to search an element in
lesser than O(N) time so what should come to your mind is that we do that using binary search
but we need a sorted array and the array we are given was sorted but it is now a little different
You have to go from there and understand that the array ust have been rotated across
a pivot and that the left and right halfs to the pivot must be sorted and you can do binary search there
"""
# The pivot is the element whose next elemet is smaller than the pivot, 3 4 5 1 2, here 5 is the pivot and 1 is the element next to it.
"""
So what  happens is that:
we find the pivot in OlogN) time and then
find the element in O(logN) time
"""

def binarySearch(arr,start,end,element):
    if start>end:
        return -1
    mid=(start+end)//2
    if element==arr[mid]:
        return mid
    if element>arr[mid]:
        return binarySearch(arr,mid+1,end,element)
    return binarySearch(arr,start,mid-1,element)
        

def findPivot(arr,start,end):
    print(arr,start,end)
    if start >= end:
        return -1
    mid=(start+end)//2
    if mid<end and arr[mid]>arr[mid+1]:
        return mid
    if mid>start and arr[mid-1]>arr[mid]:
        return mid-1
    if arr[start]>arr[mid]:
        return findPivot(arr,start,mid-1)
    return findPivot(arr,mid+1,end)
    
def findIndex(arr,element):
    if len(arr)<=0:
        return "No array"
    start=0
    end=len(arr)-1 
    pivot=findPivot(arr,start,end)
    print(pivot)
    if(pivot==-1):
        return binarySearch(arr,start,end,element)
    if(arr[pivot]==element):
        return pivot
    if element >= arr[0]:
        return binarySearch(arr,start,pivot-1,element)
    return binarySearch(arr,pivot+1,end,element)
if __name__=="__main__":

    arr=list(map(int,input("Enter the elements: ").split()))
    element=int(input("Enter the element whose index you want to find: "))
    index=findIndex(arr,element)
    print("Index: ",index)
