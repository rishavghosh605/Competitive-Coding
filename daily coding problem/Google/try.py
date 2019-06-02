def lengthLongestPath(s):
    """
    :type input: str
    :rtype: int
    """
    res = 0
    lst = s.split('\n')
    path = []
    for s in lst:
        curr_level = 0
        while s[curr_level] == '\t':
            curr_level += 1
        name = s[curr_level:]
        if '.' in name: # it is a file
            file_path = '/'.join(path[:curr_level] + [name])
            print(file_path)
            #print(file_path)
            res = max(res, len(file_path))
        else:
            if curr_level + 1 > len(path):
                path.append(name)
            else:
                path[curr_level] = name
                path = path[:curr_level+1]
    print(res)


n=input()
lengthLongestPath(n)
