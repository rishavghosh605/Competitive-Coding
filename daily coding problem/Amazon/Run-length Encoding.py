# This method is to encode the string
def encode(enc):
    # If there is not string to iterate through and decode then we return "Not Found"
    if len(enc)==0:
        return "Not Found"
    # I basically store the first character inside the result list and then iterate through the entire
    # enc string to update the count and if the current character ids different from the last character
    # of the result list and then after the for loop I add the final pair of character an its cout which
    # could not be iterated by the for loop
    result=[]
    count=0
    result.append(enc[0])
    count+=1
    for i in enc[1:]:
        if i!=result[-1]:
            result.insert(len(result)-1,str(count))
            count=1
            result.append(i)
        else:
            count+=1    
    result.insert(len(result)-1,str(count))
    return ''.join(result)

# This method is to decode the string 
def decode(dec):
    if len(dec)<2:
        return "Not Found"
    # If you are using step and you must check once if all the values you need are being taken into account or not
    result=""
    for i in range(0,len(dec),2):
        # In python we can just multiply a string with a constant and get a*2=aa
        result += dec[i+1]*int(dec[i])
    return result
        
# It will be better if I use a list to insert the count value than using a string to splice the result string in two
# parts then add count to the second part and then add them back up as splicing takes three operations whereas insert
# is only one line, both of them have O(n) time complexity but with lists the code looks much cleaner.


if __name__=="__main__":

    enc=input("Enter the string you want to encode: ")
    print("The encoded string is: ",encode(enc))
    dec=input("Enter the string you want to decode: ")
    print("The decoded string is: ",decode(dec))
