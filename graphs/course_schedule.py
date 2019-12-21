class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]
        for src, dest in prerequisites:
            adjList[dest].append(src)
        # print(adjList)
        visited = [-1] * numCourses
        timestamp = [0]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses

        def dfs(source):
            arrival[source] = timestamp[0]
            timestamp[0] += 1
            visited[source] = 1

            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    if dfs(neighbor):
                        return True
                else:
                    if departure[neighbor] == -1:
                        return True

            departure[source] = timestamp[0]
            timestamp[0] += 1
            return False

        for v in range(numCourses):
            if visited[v] == -1:
                if dfs(v):
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()

    numCourses = 2
    prereqs = [[1, 0]]
    print("possible? {}".format(solution.canFinish(numCourses, prereqs)))

    prereqs = [[1, 0], [0, 1]]
    print("possible? {}".format(solution.canFinish(numCourses, prereqs)))
