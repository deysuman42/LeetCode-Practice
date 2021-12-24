class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
      
        h = collections.Counter(arr1)
        out = []
        
        for i in arr2:
            out += [i] * h[i]
            del(h[i])
        
        h = dict(sorted(h.items()))
        
        for k, v in h.items():
            out += [k] * v
        # out += h.keys()
        return out
        # for x in h:
        #     print(x[0])
        #     out += x[0]
        # return out
      
      
        