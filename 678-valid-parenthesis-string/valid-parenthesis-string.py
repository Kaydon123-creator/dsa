class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        open = [] 

        for i in range(len(s)):
            if s[i] == ")":
                if open:
                    open.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
                    
            else:
                if s[i]=="(" :
                    open.append(i)
                else:
                    stars.append(i)
            
        while open and stars:
            if open[-1] > stars[-1]:
                return False
            open.pop()
            stars.pop()
        return True if not(open) else False

        

        
        
        