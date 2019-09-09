class Node(object):
    def __init__(self,v=None):
        self.val=v
        self.next=None
        self.prev=None

class SinglyLinkedList(object):
    def __init__(self,start=None):
        self.head=None

class DoublyLinkedList(object):
    def __init__(self,start=None,end=None):
        self.head=None
        self.tail=None

def createSinglyLinkedList(head,l):
    for i in l:
        if head!=None:
            node=Node(i)
            node.next=head
            head=node
        else:
            head=Node(i)

def createDoublyLinkedList(head,tail,l):
    for i in l:
        if head==None and tail==None:
            head=Node(i)
            tail=Node(i)
        else:
            node=Node(i)
            node.next=head
            head.prev=node


def isDPalindrome(head,tail):
    i=head
    j=tail
    while i!=j or i.next==j.prev:
        if i.val!=l.val:
            return False
        i=i.next
        j=j.prev
    return True

def isSPalindrome(head):
    mid=head
    end=head
    flag=1
    while end.next!=None:
        if end.next.next==None:
            end=end.next
            mid=mid.next
            flag=0
        mid=mid.next
        end=end.next.next
    node1=head
    node2=mid if flag==0 else mid.next
    while node2!=end:
        if node1.val!=node2.val:
            return False
        node1=node1.next
        node2=node2.next
    return True

if __name__=="__main__":

    l1=list(map(int,input("Enter the list 1: ").split()))
    l2=list(map(int,input("Enter the list 2: ").split()))
    sl=SinglyLinkedList()
    dl=DoublyLinkedList()
    createSinglyLinkedList(sl.head,l1)
    createSinglyLinkedList(dl.head,l2)
    print("For doubly linked list: ",isDPalindrome(dl.head,dl.tail))
    print("For singly linked list: ",isSPalindrome(sl.head))
