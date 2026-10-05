class MinStack:

    def __init__(self):
        self.list = []
        

    def push(self, val: int) -> None:
        if not self.list:
            self.list.append((val, val))
            return 
        self.list.append((val, min(val, self.list[-1][1])))
        
        
        

    def pop(self) -> None:
        self.list.pop()

        

    def top(self) -> int:
       
        return self.list[-1][0]
        

    def getMin(self) -> int:
       
        return self.list[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()