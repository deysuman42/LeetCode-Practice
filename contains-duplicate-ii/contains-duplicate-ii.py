class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        h = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in h:
                h[nums[i]] = [i]
            else:
                if abs(i - h[nums[i]][-1]) <= k:
                    return True
                else:
                    h[nums[i]] = [i]
        
        return False
        