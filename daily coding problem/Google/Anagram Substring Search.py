"""
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""
M=256
l=[]
def compare(sCount,pCount):

    for i in range(M):
        if sCount[i]!=pCount[i]:
            return False
    return True
    
def findIndex(S,W):
    if len(S)==1 and len(W)==1:
        return 0 if S[0]==W[0] else -1
    
    if len(S)<len(W):
        return -1

    sCount=[0]*M
    pCount=[0]*M

    for i in range(len(W)):
        pCount[ord(W[i])]+=1
        sCount[ord(S[i])]+=1

    for i in range(len(W),len(S)):
        if compare(sCount,pCount):
            l.append(i-len(W))

        sCount[ord(S[i])]+=1
        sCount[ord(S[i-len(W)])]-=1

    if compare(sCount,pCount):
        l.append(len(S)-len(W))

    return l
    
if __name__=="__main__":

    S=input("Enter the string: ")
    W=input("Enter the word: ")

    print(findIndex(S,W))
