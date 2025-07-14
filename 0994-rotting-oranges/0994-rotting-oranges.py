class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        minutes = 0
        curRotList = []
        nextRotList = []
        goodNum = 0
        

        # 将所有烂橘子加入rotList,统计好橘子数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    curRotList.append([i,j])
                if grid[i][j] == 1:
                    goodNum += 1
        if goodNum == 0:
            return 0
        # 对于每个烂橘子，使其上下左右的新鲜橘子变成烂橘子
        goodNum = [goodNum]
        def doRot():
            for location in curRotList:
                row = location[0]
                col = location[1]
                if row > 0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    nextRotList.append([row-1,col])
                    goodNum[0] -= 1
                if col > 0 and grid[row][col-1] == 1:
                    grid[row][col-1] = 2
                    nextRotList.append([row,col-1])
                    goodNum[0] -= 1
                if row < m-1 and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    nextRotList.append([row+1,col])
                    goodNum[0] -= 1
                if col < n-1 and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    nextRotList.append([row,col+1])
                    goodNum[0] -= 1

        while goodNum[0] > 0:
            nextRotList = []  # \U0001f501 这里要清空
            doRot()
            if not nextRotList:  # 如果这一轮没有新橘子腐烂，说明不能继续了
                return -1
            curRotList = nextRotList
            minutes += 1
        return minutes


                        

            


