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

class Trie:
    # A dictionary is created
    head={}
    head['*']={}

    # To add words to the tree
    def add(self,word):
        
        cur=self.head
        cur=cur['*']
        print(cur,word)

        for ch in word:
            if ch not in cur.keys():
                cur[ch]={}
            cur=cur[ch] # Now we have the cur starting at the current character in the word used by the for loop
        cur['*']=True
        '''{} # This is before the word 'hi' is inserted
            {'h': {'i': {'*': True}}} # After inserting 'hi' as you can see a
                dictionary of dictionaries is created abstracting it to give
                the feel of a tree hence the name.
        '''

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

# {'*': {'h': {'i': {'*': True}, 'e': {'l': {'l': {'o': {'*': True}}}}}}} This is the entire tree
# consisting of hi and hello
'''dictionary=Trie()
dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.head)
print(dictionary.search("hey"))
''' 
