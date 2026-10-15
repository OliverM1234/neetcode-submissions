class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        print(intervals)

        out = [intervals[0]]
        i = 1

        while i < len(intervals):

            st, en = out[-1]

            if en >= intervals[i][0]:
                out[-1][1] = max(intervals[i][1], out[-1][1])
            else:
                out.append(intervals[i])

            i += 1

        return out
        