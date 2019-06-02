'''Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.'''

import itertools
class Trie(object):
    # A dictionary is created
    def __init__(self):
        self.head={}
        self.head['*']={}
        self.size=0
    def get_head(self):
        return self.head
    def add(self,word):
        self.size+=1
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
        print(cur)
        if cur.items()!=None:
            def get_suffix(cur):
                flag=0
                if '*' in cur.keys() and len(cur.keys())==1:
                    return [""]
                suffixes=[]
                suffix=[]
                print(cur.keys())
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
'''def get_suffix(cur):
    if '*' in cur.keys():
        return [""]
    suffixes=[]
    suffix=[]
    for ch in cur.keys():
        suffix=list(map(lambda suffix: ch + suffix, get_suffix(cur[ch])))
        suffixes.append(suffix)    
    suffixes=list(itertools.chain.from_iterable(suffixes))
    return suffixes'''


    
if __name__=="__main__":        
    dictionary=Trie()
    print(dictionary.get_head())
    dictionary.add("the")
    dictionary.add("quick")
    dictionary.add("brown")
    print(dictionary.find_words("q"))


 
