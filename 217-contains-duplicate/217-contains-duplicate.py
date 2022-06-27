class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        h = collections.Counter(nums)
        for i in h.values():
            if i > 1:
                return True
        return False
      