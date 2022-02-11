class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        h_s1 = Counter(s1)
        h_s2 = Counter()
        h_s2[s2[0]] += 1 
        prev_key = s2[0]
    
    
        for i in range(0, len_s2- (len_s1 - 1)):
            
            temp = s2[i:i+len_s1]
            if Counter(temp) == h_s1:
                return True
            
        return False
            
#             if len(h_s1.keys()) == len(h_s2.keys()):
                
#                 if 
                
            
#             if h_s1 == h_s2:
#                 return True
#             if len()
            
        