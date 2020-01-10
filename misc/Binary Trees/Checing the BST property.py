class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)

        elif data>cur_node.data:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)

        else:
            
            print("The value is already present in the binary search tree")

    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self,data,cur_node):
        if data> cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data<cur_node.data and cur_node.left:
            return self._find(data,cur_node.left)
        if data==cur_node.data:
            return True

    def inorder_print_tree(self):
        if self.root:
            return self._inorder_print_tree(self.root)
        else:
            return None
    def _inorder_print_tree(self,cur_node):
        result=""
        if cur_node:
            result+=self._inorder_print_tree(cur_node.left)
            result+=str(cur_node.data)+" "
            result+=self._inorder_print_tree(cur_node.right)
            return result
        return result

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied=self._is_bst_satisifed(self.root,self.root.data)
            if is_satisfied:
                return True
        return True

    def _is_bst_satisifed(self,cur_node,data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst_satisifed(cur_node.left,cur_node.left.data)
            else:
                return False

        if cur_node.right:
            if data<cur_node.right.data:
                return self._is_bst_satisifed(cur_node.right,cur_node.right.data)
            else:
                return False
            
    def check_bst_property(self):
        if self.root:
            min=float('-inf')
            max=float('inf')
            return self._check_bst_property(self.root,min,max)
        return None

    def _check_bst_property(self,node,min,max):
        if(node == None):
            return True
        if(node.data<=min or node.data>max):

            return False
        return self._check_bst_property(node.left,min,node.data) and self._check_bst_property(node.right,node.data,max)
##        if inorder_traversal:
##            inorder_traversal=list(map(int,inorder_traversal.strip().split(" ")))
##            print(inorder_traversal)
##            for i in range(1,len(inorder_traversal)):
##                #print(i,inorder_traversal[i])
##                if inorder_traversal[i]<inorder_traversal[i-1]:
##                    return False
##        return True
        

if __name__=="__main__":
##    bst=BST()
##    bst.insert(4)
##    bst.insert(2)
##    bst.insert(8)
##    bst.insert(10)
##    bst.inorder_print_tree()
##    #print(bst.is_bst_satisfied())
##    print("Is BST: ",bst.check_bst_property())
    print("--------")
    b=BST()
    b.root=Node(10)
    b.root.left=Node(-10)
    b.root.left.left=Node(-20)
    b.root.left.right=Node(0)
    b.root.right=Node(19)
    b.root.right.left=Node(17)
    b.root.right.right=Node(20)
    b.inorder_print_tree()            
    #print(b.is_bst_satisfied())
    print("Is BST: ",b.check_bst_property())
