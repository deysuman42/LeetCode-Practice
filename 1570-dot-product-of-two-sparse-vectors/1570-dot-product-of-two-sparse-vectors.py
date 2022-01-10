class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {i:x for i, x in enumerate(nums) if x != 0}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key, value in vec.seen.items():
            if key in self.seen:
                res += value * self.seen[key]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)