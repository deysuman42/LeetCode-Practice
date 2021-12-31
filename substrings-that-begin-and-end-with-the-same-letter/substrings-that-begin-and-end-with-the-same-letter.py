class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        
        ans = 0
        h = defaultdict(int)
        
        for i in s:
            h[i] += 1
            ans += h[i]
        
        return ans
    
    