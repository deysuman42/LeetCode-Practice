class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        h = defaultdict(int)
        res = 0
        for i in time:
            if i % 60 == 0:
                res += h[0]
            else:
                res += h[60 - (i % 60)]
            h[i % 60] += 1
        
        return res