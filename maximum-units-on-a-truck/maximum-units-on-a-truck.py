class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)
        units = 0
       
        for x, y in boxTypes:
            
            if truckSize >= x:
                truckSize = truckSize - x
                units += x * y
            else:
                units += truckSize * y
                break;
            
            
        return units
            