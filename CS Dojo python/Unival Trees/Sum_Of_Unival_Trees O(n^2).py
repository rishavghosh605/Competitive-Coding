    class Node(object):
    def __init__(self,d,l=None,r=None):
        self.data=d
        self.l=None
        self.r=None
    def add(self,d,l,r)
    
class Tree(object):
    def __init__(self,r=None):
        self.root=r
        self.size=0
        
    def add(self,d,l,r):
        new_node=Node(self,d,)
    


def is_unival(root):
    if root==None:
        return True # Even an empty tree is an unival tree
    if root.left!= None and root.left.value!=root.value:
        return False
    if root.right != None and root.right.value!=root.value:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    retur False

def count_univals(root):
    if root==None:
        return 0
    count=count(root.left)+count(root.right)
    if is_unival(root)==true:
        count+=1
    return count
    

if __name__=="__main__":
    print("Enter your unival tree: ")
    mytree= Tree()
    draw_tree()
    find_unival_sum()
    
# Time complexity: O(n) for  is_unival and O(n^2) for count_univals
# It is so as the is_unival function goes through the tree in O(n) and the count_univals() calls the
# function O(n)+O(n-1)+...+O(1)=O(n^2/2)~O(n^2)times as its root changes every time it is recursively
# calls so that is how reach to the above mentioned time complexity.
