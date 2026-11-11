class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encode(s):
            alpha = [0] * 26
            for char in s:
                alpha[(ord(char) - ord('a'))] += 1
            return tuple(alpha )
        hash_map = defaultdict(list) 

        for st in strs:
            hash_map[encode(st)].append(st) 
      
        return list(hash_map.values())
            
         
        