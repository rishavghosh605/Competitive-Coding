"""
This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
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
        self.head=start
        self.tail=end
# Always take the entire linked list as input and rather than storing it's head in another variable(head=sl.head cause right now sl.head is None) use sl.head
def createSinglyLinkedList(sl,l):
    for i in l:
        if sl.head!=None:
            node=Node(i)
            node.next=sl.head
            sl.head=node
        else:
            sl.head=Node(i)

def createDoublyLinkedList(dl,l):

    for i in l:
        if dl.head==None and dl.tail==None:
            dl.head=Node(i)
            dl.tail=dl.head
        else:
            node=Node(i)
            node.next=dl.head
            dl.head.prev=node
            dl.head=node
# Configure the printList manually for whichever way you want to print whichever list
def printList(ll):
    node=ll.head
    while node!=None:
        print(node.val,end='->') if node.next!=None else print(node.val)
        node=node.next
        

def isDPalindrome(head,tail):
    if head.next==None:
        return False
    i=head
    j=tail
    #print(i!=j)
    while i!=j and (i.prev!=j):
        #print("a",i.val)
        if i.val!=j.val:
            return False
        i=i.next
        j=j.prev
        #print(i.prev!=j)
    return True


def isSPalindrome(head):
    if head.next==None:
        return False
    mid=head
    end=head
    flag=1
    while end.next!=None:
        if end.next.next==None:
            end=end.next
            mid=mid.next
            flag=0
            break
        mid=mid.next
        end=end.next.next
    node1=head
    node2=mid if flag==0 else mid.next
    #print(node1.val,node2.val,mid.val,end.val)
    node2=reverseList(node2)
    while node1!=mid:
        if node1.val!=node2.val:
            return False
        node1=node1.next
        node2=node2.next
    return True

def reverseList(node):
    if node.next==None:
        return node
    if node.next.next==None:
        temp=node
        node=node.next
        node.next=temp
        return node
        #temp.next=None
    p1=node
    p2=node.next
    p3=node.next.next
    while p3.next!=None:
        p2.next=p1
        p1=p2
        p2=p3
        p3=p3.next

    p2.next=p1
    p3.next=p2
    node=p3
    return node
    '''
1 1
1 4 1
1 4 4 1
1 4 6 7 3 7 6 4 1'''

if __name__=="__main__":
    #input("Enter the list 2: ")input("Enter the list 1: ")
    l1=list(map(int,"1 4 4 1".split()))
    l2=list(map(int,"1 4 1".split()))
    sl=SinglyLinkedList()
    dl=DoublyLinkedList()
    createSinglyLinkedList(sl,l1)
    createDoublyLinkedList(dl,l2)
    print("The singly linked list: ");
    printList(sl)
    print("For doubly linked list: ");
    printList(dl)
    print("Is doubly linked list palindrome: ",isDPalindrome(dl.head,dl.tail))
    print("Is singly linked list palindrome: ",isSPalindrome(sl.head))
