"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
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
    size=int(input("Enter the size of the list: "))
    for value in range(1,size):
        if ll.start!=None:
            node=Node(value)
            node.next=ll.start
            ll.start=node
        else:
            node=Node(value)
            ll.start=node

def reverseList(ll):
    node1=ll.start
    node2=node1.next
    node3=node2.next
    node1.next=None
    while node3.next!=None:
        node2.next=node1
        node1=node2
        node2=node3
        node3=node3.next

    node2.next=node1
    node3.next=node2
    ll.start=node3
        
    
    
if __name__== "__main__":

    ll=LinkedList()
    createLinkedList(ll)
    print("The linked list: ")
    printList(ll)
    reverseList(ll)
    print("The reversed linked list: ")
    printList(ll)
    
