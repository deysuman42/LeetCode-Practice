class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        c = 0
        for i in nums:
            
            if (i > 9 and i <= 99) or (i > 999 and i <= 9999) or (i == 100000):
                c += 1
        
        return c
                
        