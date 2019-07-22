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
    # Time Complexity: O(N)
    def enqueue(self,val):
        if self.s1.size()!=0:
            while(self.s1.peek() != None):
                self.s2.push(self.s1.pop())
                
            self.s1.push(val)
            while(self.s2.peek() != None):
                self.s1.push(self.s2.pop())
        else:
            self.s1.push(val)

    # Time Complexity: O(1)        
    def dequeue(self):              
        return self.s1.pop() if self.s1.size()!=0 else "Queue Empty"        

if __name__=="__main__":

    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Popped Element: ",queue.dequeue())
    print("Popped Element: ",queue.dequeue())
