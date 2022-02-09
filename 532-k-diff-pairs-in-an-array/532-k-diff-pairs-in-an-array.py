class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h = collections.Counter(nums)
        res = 0
        for i in h:
            if (k > 0 and (i - k) in h) or (k == 0 and h[i] > 1):
                res += 1
        return res
                
    