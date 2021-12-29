class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        first_diff = arr[1] - arr[0]
        
        if len(arr) <= 2:
            return True
        
        for i in range(2, len(arr)):
            if (arr[i] - arr[i-1]) != first_diff:
                return False
        return True