"""
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def recursiveApproach(n):
    output=""
    table=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    combination1(str(n),output,table)

def combination1(n,output,table):
    if len(n)==0:
        print(output,end=",")
        return
    elements=table[int(n[0])]
    for alphabet in elements:
        combination1(n[1:],output+alphabet,table)
    
if __name__=="__main__":

    n=int(input("Enter the number: "))
    recursiveApproach(n)
    #iterativeApproach(n)
    
