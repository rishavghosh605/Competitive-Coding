'''
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

# The file path cannot have more than one 

def is_file_exist(path):

    if '.' in path:
        return 1
    else:
        return 0

def find_ts(s):
    nt=0
    for i in s:
        if i=='\t':
            nt+=1
        else:
            break
    return nt
    
def create_filesystem(path):
    path_list=path.split('\n')
    file_system={}
    file_position=0
    filename=""
    for i in path_list:
        nt=find_ts(i)
        if nt in file_system.keys():
            file_system[nt].append((i[nt:],len(file_system[nt-1])))
        else:
            file_system[nt]=[(i[nt:],len(file_system[nt-1]) if nt!=0 else 1)]
        if is_file_exist(i):
            file_position=nt
            filename=(i[nt:],len(file_system[nt-1]))
    return file_system,file_position,filename
    
def find_longest_path(path):
    file_system,path_position,filename=create_filesystem(path)
    absolute_path=[]
    absolute_path.append(filename[0])
    directory_number=filename[1]
    path_position=path_position-1
    while(path_position>=0):
    
         prev_directory=file_system[path_position][directory_number-1]
         absolute_path.append(prev_directory[0])
         directory_number=prev_directory[1]
         path_position-=1
        
        
    return "/".join(absolute_path[::-1])

if  __name__=="__main__":

    path="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    path="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    check_file=is_file_exist(path)
    create_filesystem(path)
    if check_file:
        absolute_path=find_longest_path(path)
        print("The longest absolute path is: ",absolute_path," and its length is: ",len(absolute_path))
        
    else:
        print("The longest absolute path is: ",check_file)

