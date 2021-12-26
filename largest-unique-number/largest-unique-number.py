class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        h = Counter(nums)
        largest = -1
        num = -math.inf
        
        for k, v in h.items():
            if k > num and v == 1:
                largest = k
                num = k
            
        
        return largest
        
        