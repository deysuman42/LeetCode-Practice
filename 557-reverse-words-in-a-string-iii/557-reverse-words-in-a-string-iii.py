class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = r = 0
        s += ' ' # adding a trailing space to easily code inside loop
        s1 = ''
        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                s1 += s[l:r+1][::-1]
                r += 1
                l = r
        return s1[1:] # remove the leading space in the solution
        
    