"""
This problem was asked by Google.

Calculate sum of values between two zeroes in a linked list and replace them in place
7 0 6 5 4 0 11
7 15 11
"""

class Node(object):
    def __init__(self,value=None):

        self.data=value
        self.next=None


class LinkedList(object):
    def __init__(self):
        self.start=None

def printList(ll):
    node=ll.start
    while node!=None:
        print(node.data,end='->') if node.next!=None else print(node.data)
        node=node.next

def createLinkedList(ll):
    l=list(map(int,input("Enter the values: ").split()))
    
    for value in l:
        if ll.start!=None:
            node=Node(value)
            node.next=ll.start
            ll.start=node
        else:
            node=Node(value)
            ll.start=node

def calculateandmodify(ll):

    flag=-1
    sum=0
    node=ll.start
    p=ll.start
    while node!=None:
        if node.data!=0:
            if flag==-1 and (node.next.data!=0 and node.next.data!=None) :
                p=p.next
            if flag==0:
                sum+=node.data
        else:
            if flag==-1:
                flag=0
            elif flag==0:
                
                p.next=Node(sum)
                sum=0
                p.next.next=node.next
                p=p.next
        node=node.next
                        
            
    
    
if __name__== "__main__":

    ll=LinkedList()
    createLinkedList(ll)
    print("The linked list: ")
    printList(ll)
    calculateandmodify(ll)
    print("The modified linked list: ")
    printList(ll)
    

