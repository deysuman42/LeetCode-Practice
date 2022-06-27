class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = []
        h = {}
        a = 0

        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))

            if sorted_s not in h:
                h[sorted_s] = a
                out.append([s])
                a += 1
            else:
                index = h[sorted_s]
                out[index].append(s)
        return out
                
                
                
                
        