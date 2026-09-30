class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0 
        flag = True
        while flag:
            for word in strs:
                if i > len(word)-1 or i > len(strs[0]):
                    flag = False 
                    break
                if  word[i] != strs[0][i] :
                    flag = False
                    break
            else:
                i+=1 


        
        return strs[0][:i]
        



        

        