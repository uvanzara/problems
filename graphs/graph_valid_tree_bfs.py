'''
LeetCode # 261: Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
'''

import queue


class Solution:
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    def validTree(self, n, edges):
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
        parent = [-1] * n

        def bfs(source):
            q = queue.Queue()
            q.put(source)
            visited[source] = 1
            while not q.empty():
                node = q.get()

                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        q.put(neighbor)
                    else:  # neighbor has been visited
                        if neighbor != parent[node]:
                            # found a cross edge!
                            return True
            return False

        components = 0

        for v in range(n):
            try:
                if v not in adjList.keys():
                    adjList[v] = []
            except KeyError:
                continue
            if visited[v] == -1:
                components += 1
                if components > 1 or bfs(v):
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print("Is tree = {}".format(solution.validTree(n, edges)))

    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print("Is tree = {}".format(solution.validTree(n, edges)))
