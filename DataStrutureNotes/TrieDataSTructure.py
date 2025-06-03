"""
Trie Data structure is expansion of tree data structure. It is used to store dynamic set of strings. 
It helps in quickly find the words existing on the branch. 

insert a word , delete a word, search a word. 
Design type ahead or auto complete systems.
given set of word and find word with given Prefix. 
Starts with this word. 

two member function or variable. 
assume all the char is lower case. we have 26 chars . 
array of size 26 and boolean flag.

intially root have array have size 26 and flag. 

now when we insert 1st word we start with the root. 
root have array of index 0 -> a , index 25 -> z




"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        newNode = self.root
        for char in key:
            if char not in newNode.children:
                newNode.children[char] = TrieNode()
            newNode = newNode.children[char]
        newNode.isEndOfWord = True
    
    def search(self, key):
        newNode = self.root
        for char in key: 
            if char not in newNode.children:
                return False
            newNode = newNode.children[char]
        # is end of word is correct as words end in trie and actual word is not ended it will return false. 
        # so half words like wordss and key is word it will return false. 
        return newNode.isEndOfWord 
    
    def startsWith(self, key):
        newNode = self.root
        for char in key:
            if char not in newNode.children:
                return False
            newNode = newNode.children[char]
        return False
            

            