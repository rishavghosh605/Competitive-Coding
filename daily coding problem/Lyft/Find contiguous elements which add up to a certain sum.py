"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

from queue import Queue

def findElements(l,k):
    q=Queue()
    sum=0
    for i in l:
        if sum + i == k:
            sum+=i
            q.put(i)
            break
        elif sum + i>k:
            while sum+i>k:
                sum-=q.get()
            if sum+i==k:
                sum+=i
                q.put(i)
                break
        sum+=i
        q.put(i)
    print(sum)
    while not q.empty():
        print(q.get(),end=' ')
            
if __name__=="__main__":

    l=list(map(int,input("Enter the integers: ").split(" ")))
    k=int(input("Enter K: "))
    findElements(l,k)
    

    
