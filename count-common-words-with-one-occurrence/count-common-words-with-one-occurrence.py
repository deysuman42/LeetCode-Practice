class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        w1 = dict(collections.Counter(words1).items())
        w2 = dict(collections.Counter(words2).items())
       
        s = 0
        

        return len({w for w, v in w1.items() if v == 1} & {w for w, v in w2.items() if v == 1})
        
                
                
        