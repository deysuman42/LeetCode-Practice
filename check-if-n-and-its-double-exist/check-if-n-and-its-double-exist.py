class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        h = collections.Counter(arr)
        
        if h[0] > 1:
            return True
        
        for i in arr:
            if h[i*2] and i != 0:
                return True
        return False