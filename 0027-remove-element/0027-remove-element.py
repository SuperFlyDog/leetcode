class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0
        m = len(nums)
        i = 0
        while i < m:
            if nums[i] == val:
                del nums[i]
                i -= 1
                m -= 1
            else:
                res += 1
            i += 1

        return res