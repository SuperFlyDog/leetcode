class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # 1. Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        # 2. Initialize result list with the first interval
        merged = [intervals[0]]

        # 3. Traverse the sorted intervals and merge as needed
        for current in intervals[1:]:
            last = merged[-1]
            # If overlapping
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # merge
            else:
                merged.append(current)  # no overlap, add new interval

        return merged
