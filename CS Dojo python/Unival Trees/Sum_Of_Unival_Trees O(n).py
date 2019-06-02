''' We basically combine the two functions cunt)univals and
is_univals of 'Sum_of Unival_Tress O(n^2)'.py into one function called helper
and count_univals2 will act like an wrapper to the helper function '''

# Gives the total no. of non_empty subtrees in the tree
# A wrapper function for helper
def count_univals2(root):
    is_unival,total_count = helper(root)
    return total_count

# It will return a tuple
# ( the total no. of non_empty unival subtrees,is root a unival)
def helper(root):
    if root==None:
        return (True,0)
    #left=helper(root.left)
    #right=helper(root.right)
    is_left_unival,left_count=helper(root.left)
    is_right_unival,right_count=helper(root.right)
    is_unival=True # Rather than checking for the truth of the root node
                   # being a unival tree is easier by supposing it is then checking for conditions as to how it cannot be
    if not is_left_unival or not is_left_unival:
        is_unival=False
    if root.left!=None and root.left.vaue!=root.value:
        is_unival=False
    if root.right!=None and root.right.vaue!=root.value:
        is_unival=False
    count=left_count+right_count
    if is_unival:
        return (is_unival,count+1)
    return (is_unival,count)
        
    '''if root.left==root.right:
        if left[0] and right[0]:
            count+=left[1]+right[1]
            return (True,count)'''
    return (False,count)


# Solves in O(n)
