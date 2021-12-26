class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        h1 = dict(Counter(nums1)).keys()
        h2 = dict(Counter(nums2)).keys()
        
        return [k for k in h1 if k in h2]
        
        
        