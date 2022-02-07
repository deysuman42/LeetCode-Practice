class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # constant space becuase max 26 unique characters could be present O(1)
        # Time complexity - O(n)
#         h = collections.Counter(s)
        
#         for i in t:
#             if (i not in s) or h[i] == 0:
#                 return i
#             else:
#                 h[i] -= 1

        # Bit manipulation
        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)
        print(ch)
        for char_ in t:
            ch ^= ord(char_)
        print(ch)
        # What is left after XORing everything is the difference.
        return chr(ch)
        
        