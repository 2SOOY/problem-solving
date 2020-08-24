# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict, deque
START = 1

def generate_graph(edges):
    graph = defaultdict(list)
    
    # 양방향 그래프
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    return graph 


def bfs(n, graph, check, distances, queue):
    while queue:
        node, step = queue.popleft()

        for adj_node in graph[node]:
            if check[adj_node]:
                continue

            queue.append((adj_node, step + 1))
            distances[adj_node] = step + 1
            check[adj_node] = True
    return


def solution(n, edges):
    graph = generate_graph(edges)
    distances = [0] * (n + 1)
    check = [False] * (n + 1)

    queue = deque()
    queue.append((START, 1))
    check[START] = True

    bfs(n, graph, check, distances, queue)

    max_distance = max(distances)
    answer = [node for node, distance in enumerate(distances) if distance == max_distance]
    
    return len(answer)

n = 6
edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n , edges))