class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        
        i = 0
        xor = 0
        
        while i != n:
            num = start + ( 2 * i)
            i += 1
            xor = xor ^ num
        return xor
        