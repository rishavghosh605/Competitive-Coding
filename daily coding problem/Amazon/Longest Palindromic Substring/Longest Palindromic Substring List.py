"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""

def find_palindrome_length(s1,s2,odd_even):
    s1,s2=(s1,s2) if len(s1)>=len(s2) else (s2[::-1],s1[::-1])
    
    print("s1: ",s1," s2: ",s2)
    length=0
    palin=odd_even
    for i in range(len(s2)):
        if s2[i]== s1[len(s1)-i-1]:
            length+=1
            palin=s2[i]+palin+s2[i]
        else:
            break
    length=length*2+len(odd_even)       
    print("length: ",length,palin)
    return length,palin

def find_max_palindrome_length(s):
    max_length=0
    max_palindrome_list=[]
    for i in range(len(s)):
        length1,palin1=find_palindrome_length(s[0:i],s[i:],'')
        length2,palin2=find_palindrome_length(s[0:i],s[i+1:],s[i])
        temp_length=max(length1,length2)
        temp_palin=[]
        if len(palin1)==len(palin2):
            temp_palin.append(palin1)
            temp_palin.append(palin2)
        else:
            temp_palin.append(palin1 if len(palin1)>len(palin2) else palin2)

        if temp_length>max_length:
            max_length=temp_length
            max_palindrome_list=temp_palin
        elif temp_length == max_length:
            max_palindrome_list+=temp_palin    
            
    return max_length,max_palindrome_list
        
if __name__=="__main__":

    s=input("Enter the string: ")
    max_length,max_palindrome_list=find_max_palindrome_length(s)
    print("Max Palindrome Length: ",max_length)
    print(max_palindrome_list)
