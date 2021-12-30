class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s = 0
        p = 1
        
        q = n // 10
        r = n % 10
        
       
        
        while q > 0:
            
            s += r
            p *= r
            
            r = q % 10
            q = q // 10
            
        return (p * r) - (s + r)