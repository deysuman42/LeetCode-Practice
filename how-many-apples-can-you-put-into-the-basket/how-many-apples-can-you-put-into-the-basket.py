class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        curr_wc = 5000
        s = 0
        for i in range(len(weight)):
            curr_wc -= weight[i]
            if curr_wc >= 0:
                s += 1
            else:
                break;
            
            
        return s
        
                       
                      
            
        
        
        