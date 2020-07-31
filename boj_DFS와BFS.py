# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import defaultdict, deque


NODE_NUM, EDGE_NUM, START = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(EDGE_NUM)]

# 그래프 만들기
graph_by_list = [[0] * (NODE_NUM + 1) for _ in range(NODE_NUM + 1)]
graph_by_dict = defaultdict(list)

for start, end in edges:
    # matrix를 이용한 그래프 표현
    graph_by_list[start][end] = 1
    graph_by_list[end][start] = 1

    # dictionary를 이용한 그래프 표현
    graph_by_dict[start].append(end)


# 해당 노드 방문 여부 배열
check_dfs = [False] * (NODE_NUM + 1)
check_bfs = [False] * (NODE_NUM + 1)


# 재귀 DFS
def dfs_list(start):
    check_dfs[start] = True
    print(start, end=' ')

    for adjacent_node, connected in enumerate(graph_by_list[start]):
        if connected and check_dfs[adjacent_node] == False:
            dfs_list(adjacent_node)
    return


# BFS - matrix 그래프
def bfs_list(start):
    queue = deque()
    queue.append(start)
    _check_bfs = check_bfs.copy()

    _check_bfs[start] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=" ")

        for adjacent_node, connected in enumerate(graph_by_list[cur_node]):
            if connected and _check_bfs[adjacent_node] == False:
                queue.append(adjacent_node)
                _check_bfs[adjacent_node] = True
    return


# BFS - 딕셔너리 그래프
def bfs_dictonary(start):
    queue = deque()
    queue.append(start)
    _check_bfs = check_bfs.copy()

    _check_bfs[start] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=" ")

        for adjacent_node in graph_by_dict[cur_node]:
            if _check_bfs[adjacent_node] == False:
                queue.append(adjacent_node)
                _check_bfs[adjacent_node] = True
    return


dfs_list(START)

bfs_list(START)
bfs_dictonary(START)
