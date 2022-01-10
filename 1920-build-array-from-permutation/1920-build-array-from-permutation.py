class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        # With extra space
        res = [0 for x in range(len(nums))]
        for i in range(0, len(nums)):
            res[i] = nums[nums[i]]
        return res