class Node:
    def __init__(self,key,val=0,nxt=None,prev=None):
        self.key = key
        self.val = val 
        self.next = nxt 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.end = Node(-1,None, None) 
        self.start = Node(-1,self.end,None)
        self.end.prev = self.start
        self.capacity = capacity
    
    def add(self,node):
        prev = self.end.prev
        prev.next = node 
        node.prev = prev 
        node.next = self.end
        self.end.prev = node 
        
    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.add(self.dic[key])
            return self.dic[key].val
        return -1 

    def delete(self):
        node = self.start.next
        del self.dic[node.key]

        self.start.next = self.start.next.next
        self.start.next.prev = self.start

    def remove(self, node):
        nxt = node.next
        prv = node.prev 
        node.next = None
        node.prev = None 
        prv.next = nxt 
        nxt.prev = prv

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key,value)
        self.add(node)
        self.dic[key] = node 
    
        if len(self.dic) > self.capacity:
            self.delete() 
        

           
        
        
        
        
        
            
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)