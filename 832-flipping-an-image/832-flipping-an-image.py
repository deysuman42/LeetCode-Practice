import numpy as np
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i, a in enumerate(image):
            image[i] = image[i][::-1]
            image[i] = 1-np.array(image[i])
            image[i] = list(image[i])
        return image
        
        
        
        