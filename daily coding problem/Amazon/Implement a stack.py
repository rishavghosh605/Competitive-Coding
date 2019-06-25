"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

# The  node class:
class Node(object):

    def __init__(self,value=None):

        self.val=value
        self.next_node=None

    def get_next(self):
        return self.next_node

    def set_next(self,node=None):
        self.next_node=node
        

# The stack class:
class Stack(object):
    def __init__(self):

        self.top=-1
        self.root=None

    def push(self,val):

        newNode=Node(val)
        if self.top!=-1:
            newNode.set_next(self.root)
            self.root=newNode
        else:
            self.root=newNode

        self.top+=1

    def pop(self):

        if self.top!=-1:
            popped=self.root.val
            self.root=self.root.get_next()
            self.top-=1
            return popped
        return None

    def max(self):

        if self.top!=-1:
            return self.top+1
        return None
    
if __name__=="__main__":
    
    stack=Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    popped=stack.pop()
    print("Popped Element: ",popped)
    popped=stack.pop()
    print("Popped Element: ",popped)
    maxed=stack.max()
    print("Elements in stack:",maxed)
