class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        stop = 0
        while stop == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                stop = 1
                fast = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
