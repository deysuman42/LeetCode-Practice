class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        x = list(zip(heights, sorted(heights)))
        return sum(1 for i in range(len(x)) if x[i][0] != x[i][1])
            
           
            
            
        
        
                