def apply_dot_regex(s,regex):
    if len(regex)>1 and len(s)>1:
        if s[1]==regex[1] or s[0]==regex[1]:
            return True
    else:
        if len(s)<=1:
            return True
    return False
def apply_asterisk_regex(s,regex):

    for index in range(len(s)):
        if s[index]==regex[1]:
            return True,index+1
    return False,0

def check_with_regex(s,regex):

    while(s!=regex):
        print(s,regex)
        if regex[0]=='.':
            endornot=apply_dot_regex(s,regex)
            if endornot:
                s=s[1:],regex[1:]
            else:
                return endornot
        elif regex[0]=='*':
            endornot,position=apply_asterisk_regex(s,regex)
            if endornot:
                s=s[position:],regex[1:]
            else:
                return endornot
        else:
            if s[0]!=regex[0]:
                return False
            else:
                s=s[1:]
                regex=regex[1:]
                

if __name__=="__main__":

    regex=input("Enter the regular expression: ")

    s=input("Enter the string: ")

    result=check_with_regex(s,regex)

    print(result)

.myy
myy
maa
.m
m
