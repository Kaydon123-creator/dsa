class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        for letter in s :
            if letter=="]":
                sub = ""
                while len(stack):
                    char = stack.pop()
                    if char.isalpha():
                        sub = char + sub
                    else: 
                        if char == "[":
                            num = ""
                            while len(stack) and stack[-1].isdigit():
                                num = stack.pop() + num
                                
                            sub = int(num)*sub
                        if len(stack)!=0:
                            stack.append(sub)
                        else:
                            result += sub
                        break 
            else:
                stack.append(letter)

        return result+"".join(stack)

          


                
            
            
                
                    



        







        


    


        