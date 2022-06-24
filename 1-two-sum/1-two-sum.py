from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = defaultdict(int)
        
        for i in range(0, len(nums)):
            if (target - nums[i]) in h:
                return [i, h[target - nums[i]]]
            else:
                h[nums[i]] = i
        return []