class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        n = len(intervals)
        i = 0
        front, back = newInterval[0], newInterval[1]

        # 1) 左侧：完全在 newInterval 左边（严格小于）
        # 条件必须是 intervals[i][1] < front
        while i < n and intervals[i][1] < front:
            res.append(intervals[i])
            i += 1

        # 2) 合并：与 [front, back] 有交集（含边界相接）
        # 条件：intervals[i][0] <= back
        while i < n and intervals[i][0] <= back:
            front = min(front, intervals[i][0])
            back  = max(back,  intervals[i][1])
            i += 1

        # 合并段只追加一次
        res.append([front, back])

        # 3) 右侧：剩余区间正序加入
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
