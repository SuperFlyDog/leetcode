class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = []

        def split(h):
            if not h:
                return
            if len(h) == 1:
                res.append(h[0])
                return
            min_h = min(h)
            min_index = h.index(min_h)
            res.append(len(h) * min_h)
            split(h[:min_index])       # 左半部分
            split(h[min_index + 1:])   # 右半部分

        split(heights)
        return max(res)
