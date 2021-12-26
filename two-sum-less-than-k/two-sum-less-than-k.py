class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        # Usinf sort
        nums.sort()
        i = 0
        j = len(nums) - 1
        val = -1
        
        print(nums)
        
        while i < j:
            
            if ((nums[i] + nums[j]) < k):
                if (nums[i] + nums[j]) > val:
                    val = nums[i] + nums[j]
                i += 1
            else:
                
                j -= 1
        
        return val
        