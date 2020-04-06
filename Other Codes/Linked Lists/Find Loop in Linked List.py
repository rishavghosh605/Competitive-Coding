class Node:
    def __init__(self):
        self.next = None
        self.data = None

class LinkedList:
    def __init__(self):
        self.start = None

    def fillList(self):
        cycle = Node()
        p=self.start
        while(True):
            flag = int(input("Enter 1 if you want to quit adding"))
            n = int(input("Enter a number"))
            loop = int(input("Enter 1 if you want to create loop"))
            if(flag):
                break
            if(self.start==None):
                self.start=Node()
                self.start.data=n
                p=self.start
            else:
                p.next=Node()
                p=p.next
                p.data=n
            if loop:
                cycle=p
        p.next=cycle
    def display(self):
        counter = 0
        p = self.start
        while(p!=None and counter<10):
            print(p.data)
            p=p.next
            counter+=1

def findLoop(ll):

    a=ll.start
    b=ll.start
    result=Node()
    while True:
        if b ==None or b.next==None:
            result = "No loop"
            return result
        print(a.data,b.data)
        a=a.next
        b=b.next.next
        if a==b:
            result=a
            return result
      
    return "No Loop"
if __name__ =="__main__":

    ll = LinkedList()
    ll.fillList()
    #ll.display()
    result=findLoop(ll)
    print(result if result=="No Loop" else result.data)
