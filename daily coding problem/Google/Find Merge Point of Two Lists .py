'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

'''
Things to note:
1) A singly linked list can only have one connection that is to its next node.
2) By find merge point they have not asked  to find the node with the common value but the node from where both the lists merge
  that is the node from where both the linked lists start pointing to the same address
*3) The method solution_by_hash solves the problem in O(M+N) time and O(N) space comlpexity
but on the other hand,
*4) The method solution_by_loop solves the problem in O(M+N) time and O(1) space comlpexity.
'''

# The class Node is uild so that we can work on actual nodes that form the linked list
class Node(object):
    # A constructor is initialized with the node value and the next node pointer
    def __init__(self,value,node=None):
        self.value=value
        self.next_node=node
    # Its better to use a function to get and set the values of the attributes of a node
    def get_value(self):
        return self.value
    def set_value(self,value):
        self.value=value
    def get_nextNode(self):
        return self.next_node
    def set_nextNode(self,node):
        self.next_node=node

class LinkedList(object):

    def __init__(self,index=None):
        self.start=index
        self.size=0
    def get_size(self):
        return self.size
    def get_start(self):
        return self.start
    def add(self,value):
        newNode=Node(value)
        if self.start != None:
            traverseNode=self.start
            while traverseNode.get_nextNode()!=None:
                traverseNode=traverseNode.get_nextNode()
            traverseNode.set_nextNode(newNode)
        else:
            self.start=newNode
        self.size+=1

# We traverse the bigger list to a point where both the long and short lists become same in length decreasing our search space by a little
# then we compare eah element and we return the first value we find common if we dont find any value common then the lists are not merged
# and we return not found.
def solution_by_loop(list1,list2,d):
    #Stores the start node of the bigger list that
    startNode=list1.get_start()
    # d represents that there is a difference the two lists and it would shortenn our search space we traverse through the longer list l1 d times
    if d!=0:
        # We traverse through the longer list d times here
        for i in range(list1.get_size()):
            if i<d:
                startNode=startNode.get_nextNode()
    checkNode=list2.get_start()
    while(checkNode!=None):
        if startNode.get_value()==checkNode.get_value():
            return startNode.get_value()
        else:
            startNode=startNode.get_nextNode()
            checkNode=checkNode.get_nextNode()

    return "Not found"

def solution_by_hash(list1,list2):
    # Assuming the fact that we compare that two nodes are the same by their values and not addresses according to the above question
    check_set=set()
    traverseNode=list1.get_start()
    while(traverseNode!=None):
        check_set.add(traverseNode.get_value())
        traverseNode=traverseNode.get_nextNode()
    traverseNode=list2.get_start()
    while(traverseNode!=None):
        if traverseNode.get_value() in check_set:
            return traverseNode.get_value()
        traverseNode=traverseNode.get_nextNode()

    return "Not found"

if __name__=="__main__":

    list1=LinkedList()
    list2=LinkedList()
    l1=list(map(int,input("Enter the elements for the first list: ").split(" ")))
    l2=list(map(int,input("Enter the elements for the second list: ").split(" ")))
    for i in l1:
        list1.add(i)
    for i in l2:
        list2.add(i)
    if list1.get_size()-list2.get_size()>=0:
        result=solution_by_loop(list1,list2,list1.get_size()-list2.get_size())
    else:
        result=solution_by_loop(list2,list1,list2.get_size()-list1.get_size())
    print("The solution by loop is: ",result)
    result=solution_by_hash(list1,list2)
    print("The solution by hash is: ",result)
