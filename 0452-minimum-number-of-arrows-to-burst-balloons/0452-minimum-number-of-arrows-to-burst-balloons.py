class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 1
        points.sort(key=lambda interval: interval[1])
        print(points)
        shoot = points[0][1]
        for i in range(len(points)):
            if points[i][0] <= shoot <= points[i][1]:
                continue
            else:
                shoot = points[i][1]
                res += 1
        return res

                