class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        print(arr)
        n = len(arr)
        n_5 = int(n * 0.05)
        print(n_5)
        print(sum(arr[n_5:-n_5]))
        print(n - (n_5 * 2))
        return sum(arr[n_5:-n_5]) / (n - (n_5 * 2))
        
        