class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            h[i] = h.get(i, 0) + 1
        
        for i in t:
            if i not in h:
                return False
            else:
                h[i] -= 1
        
        for k in h.values():
            if k != 0:
                return False
        return True
        
        # return collections.Counter(s) == collections.Counter(t)
        