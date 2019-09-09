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
        

        
