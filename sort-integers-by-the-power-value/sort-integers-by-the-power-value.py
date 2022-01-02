class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        out = []
        for i in range(lo, hi + 1):
            c = 0
            j = i
            while j != 1:
                if j % 2 == 0:
                    j = j / 2
                else:
                    j = (3 * j) + 1
                c += 1
                
            out.append([c, i])
        
            
        
        res = sorted(out,key=lambda x: (x[0],x[1]))
        return res[k-1][1]
              