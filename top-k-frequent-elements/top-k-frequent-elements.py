class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         heap = []
#         for key, v in collections.Counter(nums).items():
#             heapq.heappush(heap, ([-v, key]))
            
#         print(heap)
            
#         return [x[1] for x in heapq.nsmallest(k, heap)]

        h = Counter(nums)
        n = len(nums)
        
        arr = [[] for _ in range(n+1)]
        ans = []
        
        for key, value in h.items():
            arr[value].append(key)
        
        i = 0
        for x in range(len(arr) - 1, -1, -1):
            for c in arr[x]:
                if i < k:
                    ans.append(c)
                    i += 1
                else:
                    break;
        
        return ans

#         bucket = [[] for _ in range(len(nums) + 1)]
#         Count = Counter(nums).items()  
#         for num, freq in Count: bucket[freq].append(num) 
#         flat_list = list(chain(*bucket))
#         return flat_list[::-1][:k]
        