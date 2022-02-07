class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        h = collections.Counter(s)
        
        for i in t:
            if (i not in s) or h[i] == 0:
                return i
            else:
                h[i] -= 1
        
        