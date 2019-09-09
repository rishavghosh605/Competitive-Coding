"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""
class Node(object):

    def __init__(self,value=None):

        self.data=value
        self.left=None
        self.right=None

class Tree(object):

    def __init__(self,start=None):
        self.root=None

def findDeepestNode(node):

    if node.left==None and node.right==None:
        return 1
    leftTreeHeight=1+findDeepestNode(node.left) if node.left!=None else 0
    rightTreeHeight=1+findDeepestNode(node.right) if node.right!=None else 0
    return max(leftTreeHeight,rightTreeHeight)
    

if __name__=="__main__":

    tree=Tree()
    tree.root=Node("a")
    tree.root.left=Node("b")
    tree.root.right=Node("c")
    tree.root.left.left=Node("d")
    tree.root.right.right=Node("e")
    tree.root.right.right.right=Node("f")
    print(findDeepestNode(tree.root))
