class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 替换你现在的前几行（删除 nums.append(0) 和 print）
        if not nums:
            return []
        res = []
        minList = [nums[0]]  # 用当前段的起点初始化
        # 替换 for 循环整体
        n = len(nums)
        for i in range(1, n + 1):  # 注意 i 可以等于 n，用于统一收尾
            # 还在同一段：当前值等于上一个值 + 1
            if i < n and nums[i] == nums[i - 1] + 1:
                minList.append(nums[i])
            else:
                # 这一段结束：输出 [start, end]
                a, b = minList[0], minList[-1]
                res.append(str(a) if a == b else str(a) + "->" + str(b))
                # 如果还有元素，开启新的一段
                if i < n:
                    minList = [nums[i]]

        return res

