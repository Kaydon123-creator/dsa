class Node:
        def __init__(self):
            self.childrens = {}
            self.isend = False 

class Trie:   
    def __init__(self):
        self.root = Node()
        

    def insert(self, word):
        read = 0 
        root = self.root
        while read < len(word) and word[read] in root.childrens:
            root = root.childrens[word[read]]
            read +=1 
        while read < len(word) :
            root.childrens[word[read]] = Node()
            root = root.childrens[word[read]]
            read+=1 
        root.isend = True 
    def search(self, word):

        res = self.root 
        read = 0 
        while read < len(word) and word[read] in res.childrens:
            res = res.childrens[word[read]]
            read +=1 

        return True if res.isend and len(word) == read else False 
    
    def startsWith(self, prefix):
        res = self.root 
        read = 0 
        while read < len(prefix) and prefix[read] in res.childrens:
            res = res.childrens[prefix[read]]
            read +=1  
        return True if read == len(prefix) else False

