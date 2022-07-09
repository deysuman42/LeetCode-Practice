class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r:
            
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return  res