class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jw_dict = defaultdict(int)
        stones_dict = defaultdict(int)
        
        for i in jewels:
            jw_dict[i] += 1
        for i in stones:
            stones_dict[i] += 1
        
        return sum(v for k,v in stones_dict.items() if k in jw_dict)
        