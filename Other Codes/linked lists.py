# We start out by writing a node class

class Node(object):
    # The constructor below creates a node with two arguments a data and a pointer to the next linked list
    def __init__(self,d,n=None):
        self.data=d
        self.next=n

    # Now we code up the other helper functions that a node object generally has
    def get_next(self):
        return self.next
    def set_next(self,n):
        self.next=n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data=d
    def delete(self):
        self.next=None
        self.data=None
# We then write the linked list class which is basically responsible for using the node class objects
# to create a list consisting of nodes that are joined to each other using the pointers of the node class

class LinkedList(object):
    # Every linked lit should have a pointer to the root node or th first/start node
    def __init__(self,r=None):
        self.root=r
        self.size=0 # Size of the node will obviouly be initially 0
    # Returns the size of the linked list
    def get_size(self):
        return self.size
    # Used to add a new node to the linked list **at the beginning
    def add(self,d):
        new_node=Node(d,self.root) # A new node is created with it pointing to the root node
        self.root=new_node # The new node is made the root node and the size is then incremented
        self.size+=1
    # Used to remove a node, we keep track of two consecutive nodes here so that when the node is deleted
    # then the pointer of the node previous to it will now point to the next node to the deleted node and
    # thus we break and connect two pointers to remove a node
    # Finally we return if we were successful in finding and removing the node by returning True or False
    def remove(self,d):
        this_node=self.root # The node that is to be deleted
        prev_node=None  # The node that points to the node previous to the node to be deleted
        # We search for the node using a linked list
        while this_node:
            # If we find the node having the same value that we wanted to find we check two conditions
            if this_node.get_data()==d:
                # First, if a previous node exists then the node to be delted is not a starting node
                if prev_node:
                    prev_node.set_next(this_node.get_next()) # Setting the previous node to point to the next node to the deleted node
                    this_node.delete() # We set the values of the next to None so as to delete it

                # Second, if there is no previous node then the node to be deleted is the starting node
                # so we delete the starting node and also reinitialize th linked list
                else:
                    self.root=this_node.get_next()
                    this_node.delete()
                self.size-=1 # The size is decremented after deleting the node
                return True
            # If we do not get the node at the current location we parse on or move on to the next set of nodes
            else:
                prev_node=this_node
                this_node=this_node.get_next()

        return False
    # Used to find a given node and return the value if the node is found and if the node is not found we return None
    def find(self,d):
        this_node=self.root
        while this_node:
            if this_node.get_data()==d:
                return d
            else:
                this_node=this_node.get_next()
        return None
def draw_linked_list(myList):
    myList.add(5)
    myList.add(8)
    myList.add(12)
    print("size="+str(myList.get_size()))
    myList.remove(8)
    print("size="+str(myList.get_size()))
    print(myList.remove(12))
    print("size="+str(myList.get_size()))
    print(myList.find(5))

# To use a linked list we instantiate a new linked list which in turn instantiates new nodes to form the linked list
if __name__=="__main__":
    myList = LinkedList()
    print(myList)
    draw_linked_list(myList)
    print(myList.find(5))

