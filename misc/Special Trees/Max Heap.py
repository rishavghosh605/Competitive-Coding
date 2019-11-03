""" A Max Heap is a complete binary tree where every node<=its parent
    Insert in O(log n)
    Get Max in O(1)
    Remove Max in O(logn)

    Easy to implement using an array:
    for any i index:
    parent index = i/2
    left child index = i*2
    right child inde =i*2+1

    General axHeap Operations:
    Push(insert)
    Peek(get max)
    Pop(remove max)

    Push:
    i> Add value to array
    ii> Float it up to its position

    Peek
    i> Return the value at heap[1]

    Pop
    i> Move max to end of array
    ii> Delete it
    iii> Bubble Down the item at index 1 to its proper position
    iv> Return max

"""
class MaxHeap:

    def __init__(self,items=[]):
        self.heap = [0]# We initialize the heap with a zero as
                       #we do not want to use the index 0 in our computations

        for i in items:
            self.heap.append(i)
            self._floatUp(len(self.heap)-1)

    def push(self,data):
        self.heap.append(data)
        self._floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1,len(self.heap)-1)
            max=self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            max=self.heap.pop()
        else:
            max=False
        return max

    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def _floatUp(self, index):
        parent = index//2
        if index<=1:
            return
        elif self.heap[index]>self.heap[parent]:
            self._swap(index,parent)
            self._floatUp(index)

    def _bubbleDown(self,index):
        left = index*2
        right = index*2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest=left
        if len(self.heap)>right and self.heap[largest]<self.heap[right]:
            largest=right
        if index!=largest:
            self._swap(index,largest)
            self._bubbleDown(index)
        return 

if __name__=="__main__":

    m = MaxHeap([95,3,21])
    print("Before pushing 10: ")
    print(m.heap)
    m.push(10)
    print("After pushing 10: ")
    print(m.heap)
    print("Before popping: ")
    print(m.heap)
    print(str(m.pop()))
    print("After popping: ")
    print(m.heap)
