# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

def dfs(graph, visited, i):
    visited[i] = True

    for adj_node in graph[i]:
        if visited[adj_node] == False:
            dfs(graph, visited, adj_node)


def solution(graph):
    NODES = len(graph)
    visited = [False] * NODES
    answer = 0

    for node in range(NODES):
        if visited[node] == False:
            dfs(graph, visited, node)
            answer += 1

    return answer


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    v1, v2 = v1 - 1, v2 - 1
    graph[v1].append(v2)
    graph[v2].append(v1)

print(solution(graph))