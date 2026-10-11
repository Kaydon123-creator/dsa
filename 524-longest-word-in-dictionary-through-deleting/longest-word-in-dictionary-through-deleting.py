class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        dictionary.sort(key = lambda x:(-len(x), x)) 

        for word in dictionary:
            count = 0
            for i in range(len(s)):
                if count < len(word) and s[i] == word[count]:
                    count+=1 
            if count == len(word):
                return word 
        return ""

        