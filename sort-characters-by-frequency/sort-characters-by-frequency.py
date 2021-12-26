class Solution:
    def frequencySort(self, s: str) -> str:
        
        heap = []
        out = ''
        
    
        for key, v in dict(collections.Counter(s)).items():
            heapq.heappush(heap, ([-v, key]))
            
        
        while len(heap) != 0:
            x = heapq.heappop(heap)
            out += -(x[0]) * x[1]
        return out
       
        
        