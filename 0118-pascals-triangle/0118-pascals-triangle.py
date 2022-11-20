class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        for i in range(1, numRows + 1):
            
            temp = [0] * i
            
            if i < 3:
                
                temp = [1] * i
            
            else:
                prev = res[i-2]
                temp = [0] * i
                temp[0] = 1
                temp[-1] = 1
                
                for j in range(1, len(temp) - 1):
                    temp[j] = prev[j] + prev[j - 1]
            res.append(temp)
            print(res, i)
            
        return res
        