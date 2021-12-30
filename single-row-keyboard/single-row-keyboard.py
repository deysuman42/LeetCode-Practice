class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        h = {}
        prev_ind = 0
        curr_ind = 0
        s = 0
        
        for i in range(len(keyboard)):
            h[keyboard[i]] = i
        
        for j in word:
            curr_ind = h[j]
            s += abs(curr_ind - prev_ind)
            prev_ind = curr_ind
        
        return s