class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        stack = []
        
        if len(arr) < 2:
            return [-1]
        
        for i in range(0, len(arr)-1):
            max_right = max(arr[i+1:])
            stack.append(max_right)
        stack.append(-1)
        return stack