class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        out = []
      
        if len(intervals) == 2:
            if intervals[0][1] >= intervals[1][0]:
                out.append([min(intervals[0][0],intervals[1][0]), max(intervals[0][1], intervals[1][1])])
                return out
            else:
                return intervals
            
        elif len(intervals) == 1:
            return intervals
        
        elif len(intervals) > 2:
            if intervals[0][1] >= intervals[1][0]:
                out.append([min(intervals[0][0],intervals[1][0]), max(intervals[0][1], intervals[1][1])])
            else:
                print(intervals[:2][0])
                out = intervals[:2]
            print(out)
            for i in range(2, len(intervals)):
                print(out[-1][1])
                if out[-1][1] >= intervals[i][0]:
                    out.append([min(out[-1][0],intervals[i][0]), max(out[-1][1], intervals[i][1])])
                    print(out)
                    out.pop(-2)
                    # out.append([out[-1][0], intervals[i][1]])
                else:
                    out.append(intervals[i])
            
        return out
                
            