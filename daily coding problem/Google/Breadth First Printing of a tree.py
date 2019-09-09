"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""
from queue import Queue
class Node(object):
    def __init__(self,v=None):
        self.val=v
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,start=None):
        self.root=start

def printInBFS(root):

    
    q=Queue()
    q.put(root)
    while(not q.empty()):
        node=q.get()
        print(node.val,end=" ")
        if node.left!=None:
            q.put(node.left)
        if node.right!=None:
            q.put(node.right)
        
         
if __name__=="__main__":

    bt=BinaryTree()
    bt.root=Node(1)
    bt.root.left=Node(2)
    bt.root.right=Node(3)
    bt.root.right.left=Node(4)
    bt.root.right.right=Node(5)

    printInBFS(bt.root)
