class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        n = len(nums)
        rotated_index = 0  # 默认未旋转

        if nums[0] > nums[-1]:
            left = 0
            right = n - 1
            while left < right:
                curr = (left + right) // 2
                if nums[curr] > nums[right]:
                    left = curr + 1
                else:
                    right = curr
            rotated_index = left  # 最小值位置就是旋转点
        return nums[rotated_index]