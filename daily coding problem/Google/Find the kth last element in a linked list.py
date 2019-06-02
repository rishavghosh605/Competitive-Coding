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
def add_elements(llist):
    l=list(map(int,input("Enter the elements for the singly linked list: ").split(" ")))
    for i in l:
        llist.add(i)
def find_kth_element(llist,k):
    counter=0
    kth_element=llist.get_start()
    traverse_node=llist.get_start()
    while(traverse_node!=None):
        counter+=1
        if counter>k:
            kth_element=kth_element.get_nextNode()
        traverse_node=traverse_node.get_nextNode()
    if counter>=k:
        return kth_element.get_value()
    return "Not Found"
            
    

if __name__=="__main__":

    k=int(input("Enter the value of k: "))
    linkedlist=LinkedList()
    add_elements(linkedlist)
    result=find_kth_element(linkedlist,k)
    print("The kth last element is: ",result)

