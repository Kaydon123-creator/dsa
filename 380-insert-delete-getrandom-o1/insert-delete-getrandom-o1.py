from random import choice
class RandomizedSet:
   
    def __init__(self):
        self.dic = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        index = self.dic[val]
        self.list[index], self.list[-1] = self.list[-1], self.list[index]
        new = self.list[index]
        self.dic[new] = index
        self.list.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()