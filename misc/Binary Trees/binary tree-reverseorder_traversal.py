class Queue(object):
    def __init__(self):
        self.items=[]

    def  enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return  self.size()

    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversal_type):
        if traversal_type=="reverselevelorder":
            return self.reverse_levelorder_print(tree.root)
        
        
        else:
            print("Traversal type "+str(traversal_type)+" is not supported")
            return False


    def reverse_levelorder_print(self,start):

        if start is None:
            return

        queue=Queue()
        stack=Stack()

        queue.enqueue(start)

        traversal=""
        while(len(queue)>0):
            node=queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            #Check if node.left exists
            if node.left:
                queue.enqueue(node.left)

        while len(stack)>1:

            node=stack.pop()
            traversal+=str(node.value)+"->"

        node=stack.pop()
        traversal+=str(node.value)
        return traversal
                
if __name__=="__main__":
    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    

    print(tree.print_tree("reverselevelorder"))
