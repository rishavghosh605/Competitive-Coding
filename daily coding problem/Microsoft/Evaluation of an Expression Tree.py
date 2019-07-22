


class Node:
    def __init__(self,val=None):
        self.value=val
        self.left=None
        self.right=None

def solve(left_operand,operation,right_operand):

    if operation=='/':
        return left_operand/right_operand
    if operation=='+':
        return left_operand+right_operand
    if operation=='-':
        return left_operand-right_operand
    if operation=='*':
        return left_operand*right_operand

def evaluate_tree(root):
    if root.left==None and root.right==None:
        return root.value
    left_operand=evaluate_tree(root.left)
    right_operand=evaluate_tree(root.right)
    solution=solve(left_operand,root.value,right_operand)
    return solution

def find_expression(root):
    if root==None:
        return ""
    traversal=""
    traversal=find_expression(root.left)
    traversal+=str(root.value)
    traversal+=find_expression(root.right)
    return traversal if root.left==None and root.right==None else "("+traversal+")"
    
    

if __name__=="__main__":

    root=Node('*')
    root.left=Node('+')
    root.right=Node('+')
    root.left.left=Node(3)
    root.left.right=Node(2)
    root.right.left=Node(4)
    root.right.right=Node(5)

    print("The expression to be evaluated is: ",find_expression(root))
    solution=evaluate_tree(root)
    print("The value of the evaluated expression is: ",solution)
