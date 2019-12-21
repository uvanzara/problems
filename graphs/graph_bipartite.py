'''
LeetCode # 261: Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
'''


class Solution:
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    def isBipartite(self, edges):
        adjList = edges

        print('adjList = {}'.format(adjList))
        n = len(edges)
        visited = [-1] * n
        parent = [-1] * n
        color = [-1] * n
        print('color array = {}'.format(color))

        def dfs(source):
            visited[source] = 1
            if parent[source] == -1:
                color[source] = 0
            else:
                color[source] = 1 - color[parent[source]]
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    parent[neighbor] = source
                    if not dfs(neighbor):
                        return False
                else:  # neighbor has been visited
                    if color[neighbor] == color[source]:
                        return False
            return False

        # components = 0

        for v in range(n):
            if visited[v] == -1:
                # components += 1
                if not dfs(v):
                    return False

        return True


if __name__ == "__main__":
    solution = Solution()
    graph = [[4, 1], [0, 2], [1, 3], [2, 4], [3, 0]]
    print("Is tree bipartite = {}".format(solution.isBipartite(graph)))

    edges = [[1, 3], [0, 2], [1, 3], [0, 2]]

    print("Is tree bipartite = {}".format(solution.isBipartite(edges)))

    edges = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print("Is tree = {}".format(solution.isBipartite(edges)))
