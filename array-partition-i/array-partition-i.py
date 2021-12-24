class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i = 0
        j = 1
        s = 0
        
        while j < len(nums):
            
            s += min(nums[i], nums[j])
            i += 2
            j += 2
        
        return s