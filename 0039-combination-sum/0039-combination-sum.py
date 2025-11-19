class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start,remain,path):
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return
            
            for i in range(start,len(candidates)):
                num = candidates[i]
                if num > remain:
                    break
                path.append(num)
                dfs(i,remain - num,path)
                path.pop()
        dfs(0,target,[])
        return res