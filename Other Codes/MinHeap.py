"""
We can use a class to maintain every node of a Heap
class Heap{
HeapNode left;
HeapNode right;
}
BUt we can use an array as simply using the index we can get the respective child:
parent:(index-2)/2
left child: (index*2)+1
right child: (index*2)+2
"""

class MinIntHeap:

    def __init__(self,n):

        self.capacity=n
        self.items=[0 for i in range(n)]

    def _swap(indexOne,indexTwo):

        temp=self.items[indexOne]
        self.items[indexOne]=self.items[indexTwo]
        self.items[indexTwo]=temp

    def _ensureExtraCapacity():

        if size == capacity:
            items=Arrays.copyOf
        
    def __getLeftChildIndex(int parentIndex):
        return parentIndex*2 +1;

    def __getRightChildIndex(int parentIndex):
        return parentIndex*2 +2;

    def __getParentIndex(int childIndex):
        return (childIndex-1)/2
    
    def __hasLeftChild(int index):
        return __getLeftChildIndex(index)<size

    def __hasRightChild(int index):
        return __getRightChild(index)<size

    def __hasParent(int index):
        return __getParentIndex(index)>=0

    def __letChild(int index):
        return  items[__getLeftChildIndex(index)];

    def __rigthChild(int index):
        return items[__getRightChildIndex(index)];

    def __parent(int index):
        return items[__getParentIndex(index)];
        
