# Python program to find the longest substring with k unique
# Possible characters in a given string 
max_chars=26
# Initialize associative array count[] with zero 
counter=[0]*max_chars

# This function checks if a character is unique in the current window 
# using a associative array count[]. It updates the count of the characters
# according to the current window. Returns true if 
# the character is unique else returns false.
def check_unique(ch):
    pos=ord(ch)-ord('a')
    if counter[pos]==0:
        counter[pos]+=1
        return True
    else:
        counter[pos]+=1

# Use to decide where the window should start
def cull(s0,s1):
    for i in range(s0,s1):
        if counter[ord(s[i])-ord('a')]>1:
            counter[ord(s[i])-ord('a')]-=1
        else:
            counter[ord(s[i])-ord('a')]-=1
            return i+1
    return s1
def find_substrings(s,k):
    # Otherwise take a window with zero elements in it. 
    # start and end variables
    s0=0
    s1=-1
    u=0
    sub_list=[]
    maxlen=0
    for i in range(0,len(s)):
        if check_unique(s[i]):
            u+=1
            if u<=k:
                s1+=1
            if u>k:
                # If there are more than k unique characters in 
                # current window, we remove from left side  and use cull()
                # to decide where we transfer s0 to, so as to essentially
                # remove one distinct character 
                sub_len=s1+1-s0
                if sub_len>maxlen:
                    sub_list=[s[s0:s1+1]]
                    maxlen=sub_len
                elif sub_len==maxlen:
                    sub_list.append(s[s0:s1+1])
                s1+=1
                u-=1
                s0=cull(s0,s1)
        else:
            s1+=1
    if u==k:
        sub_len=s1+1-s0
        if sub_len>maxlen:
            sub_list=[s[s0:s1+1]]
            maxlen=sub_len
        elif sub_len==maxlen:
            sub_list.append(s[s0:s1+1])
    return sub_list,maxlen

# Used to check if enough characters are unique or not
def unique_enough(s,k):
    l=len(set(list(s)))
    if l<k:
        return False
    else:
        return True
        
# Driver function 
if __name__=="__main__":
    s=input("Enter your substring: ")
    k=int(input("Enter the no. of unique characters: "))
    if unique_enough(s,k):
        substring,length=find_substrings(s,k)
        print("Max substring is: ",substring," with length ",length)
    else:
        print("Not enough unique characters")

# This code is contributed by RISHAV GHOSH


