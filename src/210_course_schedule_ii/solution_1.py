from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]

        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1

        queue = deque([])
        count = 0

        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        result = []
        while queue:
            node = queue.popleft()
            count += 1
            result.append(node)

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return result if count == numCourses else []
