class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = []
        
        j = 0
        
        for i in mat:
        
            heapq.heappush(heap, (sum(i), j))
            j += 1
         
        
        return [x[1] for x in heapq.nsmallest(k, heap)]
