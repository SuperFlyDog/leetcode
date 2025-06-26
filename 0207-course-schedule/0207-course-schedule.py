class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        for a, b in prerequisites:
            indegree[a] += 1
        print(indegree)

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        print(graph)

        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            cur = queue.pop()
            count += 1 
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return count == numCourses
        # for course in range(0, numCourses - 1):
        #     for i in prerequisites:
        #         if i[:1] == course