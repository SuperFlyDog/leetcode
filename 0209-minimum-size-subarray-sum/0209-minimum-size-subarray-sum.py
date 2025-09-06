class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        windowSum = 0
        minLen = float('inf')

        for right in range(len(nums)):
            windowSum += nums[right]

            while windowSum >= target:
                minLen = min(minLen, right-left+1)
                windowSum -= nums[left]
                left += 1
                
        return 0 if minLen == float('inf') else minLen