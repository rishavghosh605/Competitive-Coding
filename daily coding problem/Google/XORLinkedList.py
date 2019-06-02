class XORLinkedListNode(object):

    def __init__(self,val,prev_node,next_node):

        self.val=val
        self.npx=prev_node^next_node
    def get_npx(self):
       return self.npx     

class XORLinkedList(object):

    def __init__(self,start=-1):
        self.start=start
        self.size=0

    def insert(self,value):
        newNode=XORLinkedListNode(value,self.start,-1)
        self.start=newNode
        self.size+=1

    
    
        
