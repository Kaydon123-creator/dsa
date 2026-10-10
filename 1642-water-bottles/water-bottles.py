class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0 
        prev = 0 
        empty = 0 
        while numBottles:
            result+= numBottles
            empty = numBottles + prev
            numBottles = empty // numExchange 
            prev = empty % numExchange
           
        return result
        

           
        