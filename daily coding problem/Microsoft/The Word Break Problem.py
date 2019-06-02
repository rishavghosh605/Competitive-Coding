'''
How can we store words like: hello,hey ,hi

1> We could use a hash dictionary Search time complexity:O(1)
                                  Space time complexity:O(the number of words)

2> Trie has efficient space complexity with acceptable time complexity of search

Insert: O(key_length) that is O(l*n):l=average length of words, n=no. of words 
search:O(key_length)


Possible Questions asked in Interviews:
1> Generally the question has some sort of word validation to it
2>  Walk through this scrabble board and find all the words

Real time example:
    If someone types an invalid word on MS Words it immediately highlights tht it can be an invalid word

Generally to chec if a given word is a valid prefix or not, we generally want these calls to build on each other
so one thing that we can do with the trie dat structure is that we can keep state in various ways so when we look up for the
next character in the word we store where we are up in the tree as we recieve inout from the user  or maybe pass the
current node reference to the caller
'''
import itertools
class Trie:
    # A dictionary is created
    head={}
    head['*']={}

    # To add words to the tree
    def add(self,word):
        
        cur=self.head
        cur=cur['*']

        for ch in word:
            if ch not in cur.keys():
                cur[ch]={}
            cur=cur[ch]
        cur['*']=True
    
    def search(self,word):
        cur=self.head
        cur=cur['*']
        for ch in word:
            if ch not in cur.keys():
                return False
            cur=cur[ch]
        if '*' in cur.keys():
            return True
        else:
            return False
    
    def find_words(self,prefix):
        cur=self.head
        cur=cur['*']
        words={}
        words[prefix]={}
        for ch in prefix:
            if ch not in cur.keys():
                return words
            cur=cur[ch]
        if cur.items()!=None:
            def get_suffix(cur):
                flag=0
                if '*' in cur.keys() and len(cur.keys())==1:
                    return [""]
                suffixes=[]
                suffix=[]
                for ch in cur.keys():
                    if ch!='*':
                        suffix=list(map(lambda suffix: ch + suffix, get_suffix(cur[ch])))
                    else:
                        suffix=" "
                    suffixes.append(suffix)
                
                suffixes=list(itertools.chain.from_iterable(suffixes))
                return suffixes
        suffixes=get_suffix(cur)
        suffixes=list(map(lambda suffix: (prefix + suffix).strip(), suffixes))
        return suffixes

def add_words_to_dict(dictionary):
    n=int(input("Enter the number of words you want to enter to the dictionary: "))
    for i in range(n):
        dictionary.add(input("Enter a word: "))
        
def find(dictionary):
    word=input("Enter the word you want to search: ")
    print("Result: ",dictionary.search(word))


def find_the_no_sentences(s,dictionary):
    if len(s)==0:
        return 1
    counter=0
    prefix=s[0]
    words=dictionary.find_words(prefix)
    for word in words:
        if s[0:len(word)] == word:
            counter+=find_the_no_sentences(s[len(word):],dictionary)
    return counter     
def find_the_sentences(s,dictionary):
    if len(s)==0:
        return [[]]
    ordered_words=list()
    prefix=s[0]
    words=dictionary.find_words(prefix)
    for word in words:
        lists=list()
        if s[0:len(word)] == word:
            lists=find_the_sentences(s[len(word):],dictionary)
            #for l in lists:
                #l=[word]+l
                #l.insert(0,word)
            # The same as the above three lines
            _=list(map(lambda alist: alist.insert(0,word),lists))
        for l in lists:
            ordered_words.append(l)
    return ordered_words      
    
if __name__=="__main__":

    s=input("Enter the input string: ")

    # Now we create a trie data structure to make a dictionary to store all words in:
    dictionary=Trie()
    add_words_to_dict(dictionary)
    #print(dictionary.find_words("q"))
    sentences=find_the_sentences(s,dictionary)
    print(s)
    print("There are a total of ",find_the_no_sentences(s,dictionary)," sentence(s)")
    for sentence in sentences:
        print(sentence)  
    
