def isBinary(node):

    if node.left==None and node.right==None:
        return -1

    leftTree=isBinary(node.left)

    if leftTree==0:
        return 0

    rightTree=isBinary(node.right)

    if rightTree==0:
        return 0

    leftTree=1 if leftTree==None or node.left<val else 0
    rightTree=1 if rightTree==None or node.right>val else 0

    if leftTree*rightTree==1:
        return 1

    return 0


class Node(object):

    def __init__(self,value=None):

        self.val=value
        self.left=None
        self.right=None
8

class BinarySearchTree(object):

    def __init__(self,start=None):
        
        self.root=None


    def print_preorder(self,node):
        
        if node!=None:   
            self.print_preorder(node.left)
            print(node.val)
            self.print_preorder(node.right)


if __name__=="__main__":

    tree=BinarySearchTree()
    tree.root=Node(11)
    tree.root.left=Node(6)
    tree.root.right=Node(19)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(8)
    tree.root.left.left.right=Node(5)
    tree.root.right.left=Node(17)
    tree.root.right.right=Node(43)
    tree.root.right.right.left=Node(31)
    tree.root.right.right.right=Node(49)
    tree.print_preorder(tree.root)
