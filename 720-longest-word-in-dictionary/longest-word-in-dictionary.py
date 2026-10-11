class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort(key = lambda x:(-len(x),x))
        seen = set(words)
        print(words)
        for word in words:
            valid = True
            for i in range(1,len(word)):
                if word[:i] not in seen:
                    valid = False 
                    break
            if valid:
                return word
        return ""



