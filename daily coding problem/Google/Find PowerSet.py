'''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set
'''
def find_power_sets(s,i,sets):

    if i==len(s):
        print(sets)
        return
    find_power_sets(s,i+1,sets+[s[i]])
    find_power_sets(s,i+1,sets)
    
def PowerSet(s):
    index=0
    find_power_sets(s,index,[])

if __name__=="__main__":

    s=list(input("Enter the set: ").split())
    PowerSet(s)
    
