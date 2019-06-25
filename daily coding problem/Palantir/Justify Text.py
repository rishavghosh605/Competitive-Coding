'''
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenlys
'''
def justify(sentence,k,count):
    
    justified=""

    word_length=len(sentence)

    if word_length>1:

        spaces_needed=k-count

        while spaces_needed>0:
            i=1
            
            while(i!=len(sentence)):
                if spaces_needed==0:
                    break
                if sentence[i]!=' ':
                    sentence.insert(i,' ')
                    i+=1
                    spaces_needed-=1
                i+=1
                
        justified=''.join(sentence)
        
    else:
        justified=sentence[0]+ ' '*(k-len(sentence[0]))
    return justified

def create_sentences(words,k):

    sentences=[]
    count=0
    sentence=[]

    for word in words:

        if sentence==[]:
            count=len(word)

        else:
            count+=len(word)+1
            
        if count>k:
            sentences.append(justify(sentence,k,count-len(word)-1))
            sentence=[]
            count=len(word)
            
        if sentence==[]:
            sentence.append(word)
            
        else:
            sentence.append(' ')
            sentence.append(word)
    
    sentences.append(justify(sentence,k,count))
    return sentences

if __name__=="__main__":

    words=input("Enter the words with a space in betwee each of them: ").split(' ')
    k=int(input("Enter the length of a justified sentence: "))
    sentences=create_sentences(words,k)
    print(sentences)
    
