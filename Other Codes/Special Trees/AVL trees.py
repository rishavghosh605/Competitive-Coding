"""AVL Trees hae four types of rotation which get triggered on each set
of three nodes(left,right,parent) when the balancing factor(height of left subtree - height of right subtree) for their
parent is greater than 1 or lesser than -1, safe zone is [-1,1].


Four imbalance:
i> LL imbalance solved by left rotation
ii> LR imbalance solved by two rotations:- left and then right rotation
iii> RR imbalance:- solved by right rotation
iv> RL imbalance solved by two rotations:- right and then left rotation
"""
 
class node:
    def __init__(self,value=None):
        
         # Here in the node calss we make a change of
         # adding an integer height in the node class
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None
        self.height=1#Since we add the first node at a leaf location, the height of a node at leaf location is 1
                     # So writing height=1 is correc

class AVLTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
                self.root=node(value)
        else:
                self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
                if cur_node.left_child==None:
                        cur_node.left_child=node(value)
                        cur_node.left_child.parent=cur_node # set parent
                        self._inspect_insertion(cur_node.left_child)
                else:
                        self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
                if cur_node.right_child==None:
                        cur_node.right_child=node(value)
                        cur_node.right_child.parent=cur_node # set parent
                        self._inspect_insertion(cur_node.right_child)
                else:
                        self._insert(value,cur_node.right_child)
        else:
                print("Value already in tree!")

    def print_tree(self):
        if self.root!=None:
                self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
                self._print_tree(cur_node.left_child)
                print (str(cur_node.value))
                self._print_tree(cur_node.right_child)

    def height(self):
        if self.root!=None:
                return self._height(self.root,0)
        else:
                return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def find(self,value):
        if self.root!=None:
                return self._find(value,self.root)
        else:
                return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
                return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
                return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
                return self._find(value,cur_node.right_child)

    def delete_value(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self,node):

        ## -----
        # Improvements since prior lesson

        # Protect against deleting a node not found in the tree
        if node==None or self.find(node.value)==None:
                print("Node to be deleted not found in the tree!")
                return None 
        ## -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
                current=n
                while current.left_child!=None:
                        current=current.left_child
                return current

        # returns the number of children for the specified node
        def num_children(n):
                num_children=0
                if n.left_child!=None: num_children+=1
                if n.right_child!=None: num_children+=1
                return num_children

        # get the parent of the node to be deleted
        node_parent=node.parent

        # get the number of children of the node to be deleted
        node_children=num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children==0:

                # Added this if statement post-video, previously if you 
                # deleted the root node it would delete entire tree.
                if node_parent!=None:
                        # remove reference to the node from the parent
                        if node_parent.left_child==node:
                                node_parent.left_child=None
                        else:
                                node_parent.right_child=None
                else:
                        self.root=None

        # CASE 2 (node has a single child)
        if node_children==1:

                # get the single child node
                if node.left_child!=None:
                        child=node.left_child
                else:
                        child=node.right_child

                # Added this if statement post-video, previously if you 
                # deleted the root node it would delete entire tree.
                if node_parent!=None:
                        # replace the node to be deleted with its child
                        if node_parent.left_child==node:
                                node_parent.left_child=child
                        else:
                                node_parent.right_child=child
                else:
                        self.root=child

                # correct the parent pointer in node
                child.parent=node_parent

        # CASE 3 (node has two children)
        if node_children==2:

                # get the inorder successor of the deleted node
                successor=min_value_node(node.right_child)

                # copy the inorder successor's value to the node formerly
                # holding the value we wished to delete
                node.value=successor.value

                # delete the inorder successor now that it's value was
                # copied into the other node
                self.delete_node(successor)

def search(self,value):
        if self.root!=None:
                return self._search(value,self.root)
        else:
                return False

def _search(self,value,cur_node):
        if value==cur_node.value:
                return True
        elif value<cur_node.value and cur_node.left_child!=None:
                return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
                return self._search(value,cur_node.right_child)
        return False 

def __inspect_inserion(self,cur_node,path=[]):
def _inspect_deletion(self,cur_node):
def _rebalance_node(self,z,y,x):
def _right_rotate(self,z):
def _left_rotate(self,z):
def get_height(self,cur_node):
def taller_child(self,cur_node):
        
