class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse (nums, start, end):
            while start < end:
                nums[start] ,nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            
        n = len(nums)
        k %= n  # 防止k大于数组长度
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
