"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions
it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has.
Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an
inversion.

"""
import copy
def findInversions1(l):
    inversions=0
    count=0
    for i in range(len(l)):
        for j in range(i,len(l)):
                count+=1
                if l[i]>l[j]:
                    inversions+=1
    print("Total inversions: ",inversions,"\nTotal steps taken by algorithm: ",count)

def findInversions2(l1):
    l=copy.deepcopy(l1)
    inversions=0
    count=0
    flag=0
    N=len(l)
    while True:
        flag=0
        for i in range(N-1):
            count+=1
            if l[i]>l[i+1]:
                temp=l[i]
                l[i]=l[i+1]
                l[i+1]=temp
                inversions+=1
                flag=1
        if flag==0:
            break
        N-=1
        
    print("Total inversions: ",inversions,"\nTotal steps taken by algorithm: ",count)
    
def findInversion3(l):
    # To store the count of steps taken by merge sort algo
    count=[0]
    sarr,inversions=modifiedMergeSort(l,count)
    
    print("Total inversions: ",inversions,"\nTotal steps taken by algorithm: ",count[0])
    

def modifiedMergeSort(l,count):
    if len(l)<=1:
        return l,0
    #First Half is h1:
    h1,inversions1=modifiedMergeSort(l[:len(l)//2],count)
    #Second Half is h2:
    h2,inversions2=modifiedMergeSort(l[len(l)//2:],count)
    
    sarr,countInversions=merge(h1,h2,count)
    return sarr,countInversions+inversions1+inversions2

def merge(h1,h2,count):
    
    count[0]+=1
    
    sarr=[] # The sorted array
    countInversions=0
    i=0 # To store the current index of h1
    j=0 # To store the current index of h2
    
    while i<len(h1) and j<len(h2):

        if h1[i]>h2[j]:
            countInversions+=len(h1)-i
            sarr.append(h2[j])
            j+=1
            
        elif h1[i]<h2[j]:
            sarr.append(h1[i])
            i+=1

        else:
            sarr.append(h1[i])
            i+=1
            j+=1
    # Adding all the elements of the remaining list
    sarr+=h1[i:] + h2[j:]

    return sarr,countInversions
        

if __name__=="__main__":

    l=list(map(int,input("Enter the elements: ").split(' ')))
    # Naive approach, O(N*(N+1)/2 ) O(1)
    findInversions1(l)
    # Using Insertion sort generally lesser than O((n-1)(n)/2) 0(1)
    findInversions2(l)
    # uses merge sort to get O(NlogN) on average and O(N)
    findInversion3(l)
