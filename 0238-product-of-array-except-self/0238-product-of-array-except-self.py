class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        left = 1
        right = 1
        for i in range(n):
            answer[i] = left
            left = left * nums[i]
        for j in range(n-1,-1,-1):
            answer[j] = answer[j] * right
            right = right * nums[j]
        return answer
        
