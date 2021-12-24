class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        min_diff = abs(arr[1] - arr[0])
        
        h = {}
        h[min_diff] = [[arr[0], arr[1]]]
        
        for i in range(1, len(arr) - 1):
            
            if abs(arr[i+1] - arr[i]) <= min_diff:
                min_diff = abs(arr[i+1] - arr[i]) 
                if min_diff in h:
                    
                    h[min_diff] += [[arr[i], arr[i+1]]]
                else:
                    h[min_diff] = [[arr[i], arr[i+1]]]
        print(h)
            
        return h[min_diff]
        