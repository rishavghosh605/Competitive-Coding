'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''
class Node:
    def __init__(self,value=None):
        self.value=None
        self.left=None
        self.right=None
        
def insertIntoTree(start,value):
    if value<start:
        if start.left==None:
            start.left=Node(value)
            return
        insertIntoTree(start.left,value)
    else:
        if value>start:
            if start.right==None:
                start.right=Node(value)
                return
            insertIntoTree(start.right,value)
    return "Not Possible"

def balanceTree(start):
    pass

def preorder_print(start):
    if start==None:
        return 
    print(start)
    preorder_print(start.left)
    preorder_print(start.right)
def findMedian(tree_details,value):
    
    if tree_details["start"]==None:
        tree_details["start"]=Node(value)
        
    else:
        tree_details["l"],tree_details["r"]=tree_details["l"]+1,tree_details["r"] if value < tree_details["start"] else tree_details["l"],tree_details["r"]+1
        insertIntoTree(tree_details["start"],value)
        #tree_details["start"]=balanceTree(tree_details["start"])
            
        preorder_print(tree_details["start"])
        
             
if __name__=="__main__":

    # l stores the number of elements in left subtree and r for right subtree.
    # These two variables control when we will use even or odd median formula
    tree_details={"start":None,"l":0,"r":0}

    while True:
        
        n=input("Enter an element or press quit to QUIT!!")
        if n.lower()=='q':
            break
        
        median=findMedian(tree_details,n)
        print("Median",median)
        

        

    print("Thank you for playing")
