class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = {}
        for i in range(len(nums)):
            if nums[i] not in numDict:
                numDict[nums[i]] = i
            elif nums[i] in numDict:
                if abs(numDict[nums[i]] - i) <= k:
                    return True
                else:
                    numDict[nums[i]] = i
        return False