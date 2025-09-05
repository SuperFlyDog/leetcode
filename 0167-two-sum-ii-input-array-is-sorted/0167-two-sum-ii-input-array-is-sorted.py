class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = len(numbers)
        i = 0
        j = m - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1,j+1]
            elif s < target:
                i += 1
            elif s > target:
                j -= 1