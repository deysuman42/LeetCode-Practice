class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        h = {}
        for i in range(len(nums2)):
            h[nums2[i]] = i
        return [h[i] for i in nums1]
        