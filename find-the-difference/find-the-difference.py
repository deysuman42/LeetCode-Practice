class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        for k, v in Counter(t).items():
            
            if s.count(k) != v:
                return k
        
        