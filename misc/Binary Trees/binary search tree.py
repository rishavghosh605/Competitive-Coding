'''
Types of Binary Trees:
i)  Full: One where all leaf nodes are at the same level
ii) Complete: One where all levels of the tree are filled except the last level.
"All Complete binary trees are complete but all full trees are not complete."
iii) Balanced: The leaf nodes are always at the same level.

Comlpexity:
        Average   Worst
Space   O(n)      O(n)
Access  O(logn)   O(n)
Search  O(logn)   O(n)
Insertion O(logn) O(n) 
Deletion  O(logn) O(n)

'''

class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root) # Python does not have any explicit private functions but putting an
                           # '_' before insert  shoes that it is a private function and that the user must refrain from using it outside the class

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value,cur_node.left_child)
        else:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value,cur_node.right_child)

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    # Creating a function that cintrols the height of the tree
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0
    def _height(self,cur_node,cur_height):
        if cur_node==None:
            return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree

def insert_tree(tree,l):
    for i in l:
        tree.insert(i)
tree = binary_search_tree()
#fill_tree(tree)
l=list(map(int,input("Enter the values: ").split()))
insert_tree(tree,l)
tree.print_tree()
print(tree.root.value)
print("Tree height: "+str(tree.height()))
            
