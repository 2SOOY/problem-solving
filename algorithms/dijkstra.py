# Dijkstra's algorithm
# O(E*logE)
# 모든 EDGE 체크 * Min heap 정렬
import heapq


def dijkstra(graph, start):
    costs = {node: (float('inf'), start) for node in graph}  # 각 지점에 대한 비용 dict
    queue = []  # 우선순위 큐 : (비용, 경유노드)
    costs[start] = (0, start)
    heapq.heappush(queue, (costs[start][0], start))

    # 비용이 낮은 것에 대해 BFS
    while queue:
        current_cost, current_node = heapq.heappop(queue)

        # 기존 비용이 더 작은 경우 PASS
        if costs[current_node][0] < current_cost:
            continue

        # 꺼낸 노드의 인접 노드에 대해 비용 계산
        for adjacent_node, adjacent_cost in graph[current_node].items():
            temp_cost = current_cost + adjacent_cost  # 갱신될 값 = 현재까지 비용 + 인접 노드의 비용

            # 갱신될 값이 더 작다면 해당 인접 노드 비용 갱신 & 인접 노드 큐에 삽입
            if temp_cost < costs[adjacent_node][0]:
                costs[adjacent_node] = (temp_cost, current_node)
                heapq.heappush(queue, (temp_cost, adjacent_node))

    return costs


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

dijkstra(graph, 'A')
# {'A': (0, 'A'), 'B': (6, 'C'), 'C': (1, 'A'), 'D': (2, 'A'), 'E': (5, 'D'), 'F': (6, 'E')}
