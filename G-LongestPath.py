from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)


def dfs(node, graph, dist, visited):
    if visited[node] == True:
        return dist[node]
    visited[node] = True
    for child in graph[node]:
        dist[node] = max(dist[node], 1+dfs(child, graph, dist, visited))
    return dist[node]


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    dist = [0]*(n+1)
    visited = [False]*(n+1)
    for node in range(1, n+1):
        if not visited[node]:
            dfs(node, graph, dist, visited)
    print(max(dist))


if __name__ == "__main__":
    main()
