class UnionFind(object):
    def __init__(self, n):
        # 初始化每个节点是自己的父亲
        self.parent = list(range(n))

    def find(self, x):
        # 路径压缩查找根节点
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并两个集合，返回是否成功合并（用于判断是否成环）
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True


class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Step 1: 按边的权重升序排序（Kruskal算法）
        edges.sort(key=lambda x: x[2])
        
        uf = UnionFind(n)
        mst_weights = []

        # Step 2: 构建最小生成树（MST），用并查集避免成环
        for u, v, w in edges:
            if uf.union(u, v):
                mst_weights.append(w)
                if len(mst_weights) == n - 1:
                    break  # MST最多n-1条边

        # Step 3: 删除最大权重的k-1条边，将MST拆成k个连通块
        mst_weights.sort(reverse=True)
        for _ in range(k - 1):
            if mst_weights:
                mst_weights.pop(0)

        # Step 4: 返回剩下边中最大的权重，即最终的最小最大代价
        return max(mst_weights) if mst_weights else 0
