class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        compteur = 0 
        if " " not in s:
            return len(s)


        for i in range(len(s) - 1, -1, -1) :
            if s[i] == " ":
                continue 
            debut = i 
    
            while not( s[debut] == " ") :
                debut -= 1 
                compteur += 1 
            return compteur
                

        