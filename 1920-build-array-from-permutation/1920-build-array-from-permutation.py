class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        #Without extra space
        n = len(nums)
        for i in range(0, len(nums)): 
            nums[i] = nums[i] + (n * (nums[nums[i]] % n))
        
        for i in range(0, len(nums)):
            nums[i] = nums[i] // n
              
        return nums
    
    
        # With extra space
        # res = [0 for x in range(len(nums))]
        # for i in range(0, len(nums)):
        #     res[i] = nums[nums[i]]
        # return res