class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}
        for i in range(0, len(strs)):
            res = ''.join(sorted(strs[i]))
            print(res)
            if res in h:
                h[res].append(strs[i])
            else:
                h[res] = [strs[i]]
        
        return [v for k, v in h.items()]
            