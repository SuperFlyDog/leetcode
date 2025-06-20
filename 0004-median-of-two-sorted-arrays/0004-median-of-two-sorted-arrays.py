class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n%2 == 0:
            median = (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        else:
            median = merged[n // 2]
        return median


