class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palidrom(debut, end):
            left = debut
            right = end
            while left < right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True 
        
        for i in range(len(s)//2):
            if s[i]!= s[len(s)-i-1]:
                if check_palidrom(i,len(s)-i-2) or check_palidrom(i+1,len(s)-i-1) :
                    return True 
                else:
                    return False
        else:
            return True


            