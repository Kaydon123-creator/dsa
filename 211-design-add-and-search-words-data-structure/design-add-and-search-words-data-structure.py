class Node:
    def __init__(self):
        self.isend = False
        self.childrens = {}       #key: string , value:Node()



class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.childrens:
                root.childrens[c] = Node()
            root = root.childrens[c]
        root.isend = True

    @staticmethod
    def recursive_search(root,word) -> bool:
        res = root
        read = 0 
        for i,c in enumerate(word):
            if c == ".":
                for node in res.childrens:
                    if WordDictionary.recursive_search(res.childrens[node],word[i+1:]):
                        return True
            if c not in res.childrens:
                return False
            res = res.childrens[c]
        return res.isend
        

    def search(self, word):
        return self.recursive_search(self.root, word)
         

        
   


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)