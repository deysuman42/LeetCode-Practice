class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        
        # using hashmaps
#         h = collections.Counter(arr1).keys()
        
#         return [i for i in h if i in arr2 and i in arr3]
    
        # using Set
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))
        
