class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        if x < 0:
            return False 

        reverse = 0 
        while reverse < x:
            reverse = reverse*10 + x%10
            x//=10 
        
        
        return True if x == reverse or x == (reverse //10) else False

        
        
        