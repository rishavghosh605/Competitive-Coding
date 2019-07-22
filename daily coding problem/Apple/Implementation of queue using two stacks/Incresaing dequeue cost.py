"""
This problem was asked by Apple.

Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods: enqueue,
which inserts an element into the queue, and dequeue, which removes it.
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1] if len(self.items) > 0 else None

     def size(self):
         return len(self.items)

class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
    # Time Complexity: O(1)
    def enqueue(self,val):
        self.s1.push(val)

    # Time Complexity: O(N)        
    def dequeue(self):

        if self.s2.size()==0:
            if self.s1.size()==0:
                return "Queue is Empty"
            else:
                while(self.s1.peek() != None):
                    self.s2.push(self.s1.pop())
                    
        return self.s2.pop()        

if __name__=="__main__":

    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Popped Element: ",queue.dequeue())
    print("Popped Element: ",queue.dequeue())
    
