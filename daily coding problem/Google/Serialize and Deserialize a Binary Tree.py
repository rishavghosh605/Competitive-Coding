'''This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left''''


class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root==None:
        return " -1"
    
    result=" "+root.val
    result+=" "+root.left.val+serialize(root.left)
    result+=" "+root.right.val+serialize(root.right)
    return result

def deserialize(s):
    if s[0]=="-1"
        return s[1:]
    Tree.add(root)
    s=deserialize(s[1:])
    s=deserialize(s)
    return s
    
    
    
if __name__=="main":
    
    node=Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    
