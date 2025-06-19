class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 在末尾加一个 0 高度柱子，确保所有柱子都会被处理
        heights.append(0)
        stack = [-1]  # 初始化栈，存放的是下标。栈底是哨兵 -1，便于处理宽度
        max_area = 0

        for i in range(len(heights)):
            # 当前柱子比栈顶矮，说明栈顶柱子右边界到了，开始出栈
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]  # 弹出栈顶元素的高度
                width = i - stack[-1] - 1       # 当前 i 是右边界，新的栈顶是左边界
                max_area = max(max_area, height * width)
            stack.append(i)  # 当前柱子入栈

        return max_area
