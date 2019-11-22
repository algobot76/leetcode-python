from typing import List


class Solution:
    def criticalConnections(self, n: int,
                            connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        idx = [0]
        low_links = [0] * n
        lookup = [False] * n
        ans = []
        self.tarjan(graph, -1, 0, idx, low_links, lookup, ans)

        return ans

    def tarjan(self, graph: List[List[int]], parent: int, u: int,
               idx: List[int], low_links: List[int], lookup: List[bool],
               ans: List[List[int]]) -> None:
        if lookup[u]:
            return

        lookup[u] = True
        curr_idx = low_links[u] = idx[0]
        idx[0] += 1
        for v in graph[u]:
            if v == parent:
                continue
            self.tarjan(graph, u, v, idx, low_links, lookup, ans)
            low_links[u] = min(low_links[u], low_links[v])
            if low_links[v] > curr_idx:
                ans.append([u, v])
