class Solution:
    def average(self, salary: List[int]) -> float:
        min1 = math.inf
        max1 = -math.inf
        s = j = 0
        
        for i in range(0, len(salary)):
            
            if salary[i] < min1:
                min1 = salary[i]
            if salary[i] > max1:
                max1 = salary[i]
                
        return (sum(salary) - min1 - max1) / (len(salary) - 2)