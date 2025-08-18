class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]
        mn = nums[0]
        ans = nums[0]

        # 遍历 i 从 1 到 n-1
        for a in nums[1:]:
            # 使用上一步的 mx, mn 生成三个候选
            cand1 = a
            cand2 = a*mx
            cand3 = a*mn

            # 计算本轮 mx, mn
            mx = max(cand1, cand2, cand3)
            mn = min(cand1, cand2, cand3)

            # 更新答案
            ans = max(ans, mx)

        return ans