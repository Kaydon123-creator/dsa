class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""

        dic = [tuple(k) for k in knowledge]

        knowledge = {k[0]:k[1] for k in dic}
       
        opened = False
        for c in s:
    
            if c == "(":
                opened = True 
                k = ""
                continue
            if c == ")":
                res = res + knowledge[k] if k in knowledge else res + "?"
                opened = False 
                continue
      
            if opened:
                k += c 
            else :
                res+= c
            

        return res

        