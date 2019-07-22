"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""
class Node:
    def __init__(self,val=None):
        self.value=val
        self.left=None
        self.right=None
    
# This map can only work when we have only unique values in the tree
def createHashMap(inorder):
    inmap={}
    for i in range(len(inorder)):
        inmap[inorder[i]]=i

    return inmap
        
    
def buildTree(preorder,inorder):
    #Create hash map for inorder traversal
    inmap=createHashMap(inorder)
    #static variable
    _buildTree.preIndex=0
    inStart=0
    inEnd=len(inorder)-1
    root=_buildTree(preorder,inStart,inEnd,inmap)
    return root

def _buildTree(preorder,inStart,inEnd,inmap):

    if inStart>inEnd:
        return None
    
    root=Node(preorder[_buildTree.preIndex])
    inIndex=inmap[preorder[_buildTree.preIndex]]
    _buildTree.preIndex+=1
    
    # As we initialize the node with left and right child as None , if start==end then it means thae same that the node has no children so we can:
    if inStart==inEnd:
        return root
    
    root.left=_buildTree(preorder,inStart,inIndex-1,inmap)
    root.right=_buildTree(preorder,inIndex+1,inEnd,inmap)
    
    return root
    

def preorder_print(root):
    if root==None:
        return ""

    traversal=""
    traversal+=root.value
    traversal+=preorder_print(root.left)
    traversal+=preorder_print(root.right)
    return traversal

if __name__=="__main__":

    preorder=list(input("Enter the preorder traversal for the Tree").split(" "))
    print(preorder)
    inorder=list(input("Enter the preorder traversal for the Tree").split(" "))
    root=buildTree(preorder,inorder)
    print("For debugging purposes we check if the preorder traversal was correct or not: ")
    print("The preorder traversal: ",preorder_print(root))
    
