'''
LeetCode # 323: Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
This is the BFS implementation
'''


import queue


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: # noqa
        adjList = {}
        for edge in edges:
            if edge[0] not in adjList.keys():
                adjList[edge[0]] = []
            if edge[1] not in adjList.keys():
                adjList[edge[1]] = []
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        print('adjList = {}'.format(adjList))

        visited = [-1] * n

        def bfs(source):
            q = queue.Queue()
            q.put(source)

            while not q.empty():
                node = q.get()

                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.put(neighbor)

        components = 0

        for v in range(n):
            # to get the code to work on leetcode, for an input like:
            # 4
            # [[2,3],[1,2],[1,3]]
            # have to add the below code:
            try:
                if v not in adjList.keys():
                    # print('continuing for v = {}'.format(v))
                    adjList[v] = []
                    # continue
            except KeyError:
                # this is probably not necessary, but having an except doesn't
                # hurt!
                # print('KE: continuing for v = {}'.format(v))
                continue
            if visited[v] == -1:
                components += 1
                bfs(v)

        return components
