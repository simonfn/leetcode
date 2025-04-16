class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda vals : vals[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            left, right = merged[-1]
            # left <= start : since list is in ascending order
            if start <= right:
                merged[-1][1] = max(right, end)
            else:
                merged.append([start, end])

        return merged