""" Stacks and Queues:
// Animal Shelter: An animal shelter, which holds only dogs and cats operates on a strictly "first in, first
// out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
// or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
// that type). They cannot select which specific animal they would like. Create the data structures to
// maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
// and dequeueCat. You may use the built-in LinkedList data structure.
"""
# rather than only storing the order variable use it also as a global variable as it will make enqueue easier, cause then you dont need to check inside
# the lists of dog and cat for the bigger counter


class Node:
    def __init__(self,val=None,order=None):

        self.value=val
        self.next=None
        self.order=order
        
    def getOrder(self):
        return order
    def setOrder(self,order):
        self.order=order

class LinkedList:
    def __init__(self):
        self.start=None

    def enqueue(self,val,order):
        newNode=Node(val,order)
        if(self.start==None):
            self.start=newNode

        else:
            p=self.start
            while(p.next!=None):
                p=p.next
            p.next=newNode

    def dequeue(self):
        p=self.start
        if(start==None):
            return "Queue is Empty"
        elif(start.next==None):
            val=self.start.value
            self.start=None
            return val
        else:
            p=self.start
            while(p.next.next!=None):
                p=p.next
            val=p.next.value
            p.next=None
            return val

class AnimalQueue:
    def __init__(self):
        self.dog=LinkedList()
        self.cat=LinkedList()
        self.order=0

    def enqueue(self,name,val):

        if(name="dog"):
            self.order+=1
            self.dog.enqueue(val,order)
        elif(name=="cat"):
            self.order+=1
            self.cat.enqueue(val,order)
        else:
            print("Wrong List")

    def dequeueAny(self):
        pass
    def dequeueCats(self):
        pass

    def dequeueDogs(self):
        pass

        
        


if __name__=="__main__":

    queue=AnimalQueue()
    queue.enqueue('dogs',4)
    queue.enqueue('cats',7)
    queue.enqueue('cats',9)
    queue.dequeueAny()
    queue.dequeueCats()
    queue.dequeue(Dogs)
    

    
