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
        
def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree

def add_elements(tree):
    l=list(map(int,input("Enter the values: ").split()))
    for i in l:
        tree.insert(i)

def second_last_node(tree):
    if tree.root==None or (tree.root.left_child==None and tree.root.right_child==None):
        return "Not Found"
    
    value,end_reached = _second_last_node(tree,tree.root)
    return value
    
def _second_last_node(tree,cur_node):
    if cur_node == None:
        return 0,1
    large,end=_second_last_node(tree,cur_node.right_child)
    if end==1:
        if cur_node.left_child!=None:
            large=cur_node.left_child.value
            end=0
            if cur_node.left_child.right_child!=None:
                large=last_node(tree,cur_node.left_child)
        else:
            end+=1   
    elif end == 2:
        large = cur_node.value
        end=0
    return large,end

def last_node(tree,cur_node):
    if cur_node.right_child == None:
        return cur_node.value
    return last_node(tree,cur_node.right_child)

if __name__=="__main__":

    bst=binary_search_tree()
    #fill_tree(bst)
    add_elements(bst)
    bst.print_tree()
    second_largest_node=second_last_node(bst)
    print("Result:",second_largest_node)
