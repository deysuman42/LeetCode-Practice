class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        s = 0
        
        for i in Counter(nums).values():
            
            s += i * (i - 1) // 2
            
        return s
            
        
        