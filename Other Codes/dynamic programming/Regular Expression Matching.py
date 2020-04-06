def matchPattern(s,p):
    count[0]+=1
    #first do edge case check
    #if the pattern is empty then we return true if the string is also empty else we return false
    #this is used for the base case too as when ultimately the pattern gets over the sentenceshoukld also be completely matched
    if(len(p)==0):
        return len(s)==0
    #Now we know that the pattern is not empty now its turn for the string
    firstMatch = (len(s)>0 and (p[0]==s[0] or p[0]=='.'))

    if(len(p)>=2 and p[1] == '*'):#she is  using the 0 or 1 logic here in the recursion think about it
        return matchPattern(s,p[2:]) or (firstMatch and matchPattern(s[1:],p))
    else:
        return firstMatch and matchPattern(s[1:],p[1:])

def popCharacters(s,stopCharacter=None):
    c=s[0] if stopCharacter==None else stopCharacter
    index=len(s)# I initialize it as len(s) cause if I never encounter the condition s[i]!=c then I should convert s into "" as all characters match s[0]
    
    for i in range(len(s)):
        if (s[i]!=c):
            index=i
            break
    return s[index:]

def recursiveMatchPattern(s,p):
    if(len(p)==0):
        return len(s)==0
    s=" "+s
    p=" "+p
    matrix = [[False for j in range(len(p))] for i in range(len(s))]
    matrix[0][0]=True
    for i in range(len(s)):
        for j in range(1,len(p)):
            print(i,j,s[i],p[j])
            if(s[i]==p[j] or p[j]=='.' and i>0):# . cannot match a space it has to be a character
                matrix[i][j]=matrix[i-1][j-1]
            elif(p[j]=='*'):
                if(matrix[i][j-2]):
                    matrix[i][j]=matrix[i][j-2]
                elif(s[i]==p[j-1] or p[j-1]=='.'):
                    matrix[i][j]=matrix[i-1][j]
    for j in range(len(p)):
        matrix[0][j]=p[j]
    for i in range(1,len(s)):
        matrix[i][0]=s[i]
    for i in range(len(s)):
        for j in range(len(p)):
            print(matrix[i][j],end="\t")
        print("\n")

    print(matrix[-1][-1])
# the code berlow is wrong as I am checkin if character in pattern string after a* is not a then I proceed to remove all the a's but the problem is that what if a*a the condition I am checking is given in the way
# a*b*c my mistake was I reached till the a*a problem but never thought after a*b what if it was a*b* and also a*b*a
'''def matchPattern2(s,p):
    count[0]+=1
    #this is used for the base case too as when ultimately the pattern gets over the sentenceshoukld also be completely matched
    if(len(p)==0):
        return len(s)==0
    match =  (len(s)>0 and (p[0]==s[0] or p[0]=='.'))
    if(len(p)>=2 and p[1]=="*"):
        if(match):
            if len(p)>2 and p[2]==s[0]:
                return matchPattern2(s[1:],p[:2]+p[3:])
            else:
                if p[0]=='.' and len(p)>2:
                    s=popCharacters(s,p[2])
                else:
                    s=popCharacters(s) if p[0]!='.' else ""
                return matchPattern2(s,p[2:])
        else:
            return matchPattern2(s,p[2:])
    else:
        return match and matchPattern2(s[1:],p[1:]) if match else match'''

if __name__=="__main__":
    s=input("Enter the string: ")
    p=input("Enter the pattern: ")
    count=[0]
    match=matchPattern(s,p)
    recursiveMatchPattern(s,p)
    print("Match: ",match,count)
