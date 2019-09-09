paths=[]

class BinaryTree(object):
    def __init__(self,start=None):
        self.root=None

class Node(object):
    def __init__(self,value=None):
        self.val=value
        self.left=None
        self.right=None

def findPaths(node,path):
    
    if node.left==None or node.right==None:
        path+=" "+str(node.val)
        path=path.strip()
        l=list(map(int,path.split(" ")))
        paths.append(l)
        return

    path+=" "+str(node.val)

    if node.left!=None:
        findPaths(node.left,path)
    if node.right!=None:
        findPaths(node.right,path)
        
if __name__=="__main__":

    bt=BinaryTree()
    bt.root=Node(1)
    bt.root.left=Node(2)
    bt.root.right=Node(3)
    bt.root.right.left=Node(4)
    bt.root.right.right=Node(5)
    path=""
    findPaths(bt.root,path)
    print(paths)
