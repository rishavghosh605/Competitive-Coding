"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""


class Node(object):
    def __init__(self,value=None):
        self.val=value
        self.next=None

class LinkedList(object):
    def __init__(self,start=None):
        self.head=start

def add_ll(node1,node2,carry):

    if node1==None and node2==None:
        l3=LinkedList()
        
        if carry!=0:
            l3.head=Node(carry)
        return l3

    sum=0
    print(node1.val,node2.val)
    sum+=node1.val if node1!=None else 0
    sum+=node2.val if node2!=None else 0
    sum+=carry
    #Storing the zeroth index digit of sum in carry and the first index digit in sum
    carry,sum=int(str(sum)[0]),int(str(sum)[1])
    l3=add_ll(node1.next if node1!=None else node1,node2.next if node2!=None else node2, carry)
    temp=Node(sum)
    if l3.head==None:
        l3.head=temp
    else:
        temp.next=l3.head
        l3.head=temp
    return l3

def print_ll(l3):
    t=l3.head
    if l3.head==None:
        print("There is no linked list")
    else:
        while(t.next!=None):
            print(str(t.val)+"->",end="")
            t=t.next
        print(str(t.val))
    
if __name__=="__main__":

    l1=LinkedList()
    l2=LinkedList()
    l1.head=Node(9)
    l1.head.next=Node(9)
    l2.head=Node(5)
    l2.head.next=Node(2)
    carry=0
    l3=add_ll(l1.head,l2.head,carry)
    print_ll(l3)
    
