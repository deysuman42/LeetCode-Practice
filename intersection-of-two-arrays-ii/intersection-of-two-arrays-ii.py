class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Using Counter
        
        h = Counter(nums1)
        res = []
        
        for i in nums2:
            if h[i] > 0:
                res += [i]
                h[i] -= 1
        return res
        
       