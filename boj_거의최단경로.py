# 거의 최단 경로
# https://www.acmicpc.net/problem/5719
# python3 => 시간초과 / PyPy3 => 메모리 초과

from collections import defaultdict, deque
import heapq

MAX = float('inf')

def dijkstra(N, graph, src, dst, path):
    path = set(path)
    queue = []
    costs = [MAX] * N
    heapq.heappush(queue, (0, src))
    costs[src] = 0

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        # 큐 내의 우선순위에서 밀린 작업들 skip
        if cur_cost > costs[cur_node]: 
            continue

        for adj_node, adj_cost in graph[cur_node]:
            temp_cost = cur_cost + adj_cost

            # 진짜 최단 경로 => 사용 X 
            if (cur_node, adj_node) in path:
                continue
            
            if temp_cost < costs[adj_node]:
                costs[adj_node] = temp_cost
                heapq.heappush(queue, (temp_cost, adj_node))

    return costs


def check_shortest_path(N, graph_reversed, src, dst, costs):
    path = []

    # 도착 지점부터 역순으로 탐색 => 경로 check 하기
    queue = deque()
    queue.append((dst, costs[dst]))

    while queue:
        cur_node, cur_cost = queue.popleft()

        for adj_node, adj_cost in graph_reversed[cur_node]:
            # 시작 ~ 이전 노드까지의 비용 + 이전 노드 ~ 현재 노드까지 비용 == 시작 ~ 현재 노드까지의 비용
            if costs[adj_node] + adj_cost == cur_cost: 
                path.append((adj_node, cur_node))
                queue.append((adj_node, costs[adj_node]))
    
    return path

def solution(N, graph, graph_reversed, src, dst):
    path = []
    costs = dijkstra(N, graph, src, dst, path)
    path = check_shortest_path(N, graph_reversed, src, dst, costs)
    costs = dijkstra(N, graph, src, dst, path)

    answer = costs[dst]

    return -1 if answer == MAX else answer

while True:
    N, E = map(int, input().split())
    if N == 0 and E == 0:
        break

    src, dst = map(int, input().split())
    graph = defaultdict(list)
    graph_reversed = defaultdict(list)
    for _ in range(E):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        graph_reversed[end].append((start, cost))
    
    print(solution(N, graph, graph_reversed, src, dst))
