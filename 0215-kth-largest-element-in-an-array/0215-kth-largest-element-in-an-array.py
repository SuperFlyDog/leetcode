class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 建立一个大小为 k 的小顶堆
        heap = nums[:k]
        heapq.heapify(heap)       # 时间 O(k)
        # 维护堆中始终是 k 个最大的数
        for x in nums[k:]:        # 遍历剩余元素
            if x > heap[0]:       # heap[0] 是当前第 k 大
                heapq.heapreplace(heap, x)  # 弹出并推入，新元素自动调整位置
        return heap[0]
            
            
