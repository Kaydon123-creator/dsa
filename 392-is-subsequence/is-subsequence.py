class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        read = 0
        if not s :
            return True
        for i in range(len(t)):
            if read < len(s) and t[i]==s[read]:
                read+=1
        print(read)
        return read == len(s)
                 
        