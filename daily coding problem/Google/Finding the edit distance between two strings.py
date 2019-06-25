'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''
memo = {}
def levenshtein(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    if (s1,s2) not in memo.keys():
        print(s1,s2)
        memo[(s1,s2)]=min(
               # Deletion:
               levenshtein(s1[1:], s2) + 1,
               # Insertion at s1:
               levenshtein(s1, s2[1:]) + 1,
               # Substitution at any:
               levenshtein(s1[1:], s2[1:]) if s1[0] == s2[0]
                   else levenshtein(s1[1:], s2[1:]) + 1)
    return memo[(s1,s2)]

def leventshein_using_matrix(s1,s2):
    matrix=[[0]*len(s1)]*len(s2)
    for i in range(len(s2)):
        for j in range(len(s1)):
            if i==0:
                matrix[i][j]=j
            elif j==0:
                matrix[i][j]=i
            elif s2[i]==s1[j]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+1)
    print(matrix)
            
s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(levenshtein(s1,s2))
print(memo)
leventshein_using_matrix(s1,s2)
