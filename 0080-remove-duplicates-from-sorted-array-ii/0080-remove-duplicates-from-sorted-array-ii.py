class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        write = 2
        while i < len(nums):
            if nums[i] == nums[write-2]:
                i += 1
            else:
                nums[write] = nums[i]
                write += 1
                i+=1
        return write