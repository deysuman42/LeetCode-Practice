class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
        
#         len_s1 = len(s1)
#         len_s2 = len(s2)
#         h_s1 = Counter(s1)
       
#         for i in range(0, len_s2- (len_s1 - 1)):
            
#             temp = s2[i:i+len_s1]
#             if Counter(temp) == h_s1:
#                 return True
            
#         return False
            

        