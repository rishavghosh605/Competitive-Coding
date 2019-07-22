"""
This problem was asked by Google.

Implement a file syncing algorithm for two computers over a
low-bandwidth network. What if we know the files in the two computers
are mostly the same?

"""
"""
Solution


Since it is given that the network is of low-bandwidth and unreliable, it indicates that syncing of files as they are being edited is not possible or is error prone. We need a way to reliable and efficient way to sync the entire directory structure.


A point to note is that most of the directory structure is going to same, so we should prevent syncing the parts of the directory structure that are not changed.

We are going to use a data structure called """

#Merkle Tree here.

"""
Merkel Tree is a tree in which each leaf is a hash of the data block it represents and all the parent nodes are the hashes of the collated hashes of their children.

Overview of the algorithm looks as follows:
1. Whenever a change is made a file, we calculate the hashes of the entire directory branch that file part of.
2. To sync the changes, we compare the Merkle Tree of both the systems.
3. The nodes that have the same hashes can be ignored from the syncing process as the entire directory structure below them must also be the same.

The above approach can be implemented as follows:

"""

from hashlib import md5

class MerkerFile(object):

    def __init__(self):

        self.content = ""
        self.hash = ""
        self.children = []
        self.is_dir = None
        self.parent = None

    def set_content(self, new_content):

        if self.is_dir:
            raise Exception("Can't set the contents of a directory")

        self.content = new_content
        self.recalculate_directory_hash()

    def recalculate_directory_hash(self):

        parent = self.parent

        if not self.is_dir:
            self.hash = md5(self.content.encode()).hexdigest()

        while parent:
            children = parent.children
            collated_hash = ""

            for child in children:
                collated_hash += child.hash

            parent.hash = md5(collated_hash.enocde()).hexdigest()

            parent = parent.parent

    def add_file_to_directory(self,directory):

        directory.children.append(self)
        self.parent = directory

        self.recalculate_directory_hash()

    def get_files_that_are_different(root_1,root_2,file_changes_for_system_1,file_changes_for_system_2):

        if not root_1 and not root_2:
            return file_changes_for_system_1,file_changes_for_system_2

        if not root_1 or not root_2:

            file_changes_for_system_1.append(root_2)
            file_changes_for_system_2.append(root_1)
            return file_changes_for_system_1,file_changes_for_system_2

        if root_1.hash != root2.hash:
            file_changes_for_system_1.append(root_2)
            file_changes_for_system_2.append(root_1)

            len_diff=abs(len(root_1_children)-len(root_2_children))

            if len(root_1_children) > len(root_2_chuldren):
                root_2_children = root_2_children + [None for i in range(0,len_diff)]
            elif len(root_2_children) > len(root_1_children):
                root_1_children = root_2_children + [None for i in range(0,len_diff)]

            for child_1,child_2 in zip(root_1_children,root_2_children):
                get_files_that_are_different(child_1,child_2,file_changes_for_system_1,file_changes_for_system_2)
                
    return file_changes_for_system_1, file_changes_for_system_2

if __name__=="__main__":

    #create a directory structure on the first computer
    root_directory = MerkerFile()
    root_directory.is_dir = True

    file1 = MerkerFile()
    file1.is_dir = True
    file1.add_file_to_directory(root_directory)
    file1.set_content("owl city rocks")

    file2 = MerkerFile()
        
            

        
        
