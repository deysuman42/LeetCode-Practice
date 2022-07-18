class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        left = 0
        h = {}
        res = 0
        
        for i in range(len(s)):
            
            while (s[i] in h) and (h[s[i]] > 0):
                h[s[left]] -= 1
                left += 1
            h[s[i]] = 1
            res = max(res, i - left + 1)
            
        return res
        
      