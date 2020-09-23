# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

import heapq

MAX_COST = float('inf')

# 2차원 배열 이용
def networkDelayTime(times, N, K):
    SIZE = N + 1

    # 탐색을 위한 자료구조 초기화
    graph = [[-1] * SIZE for _ in range(SIZE)]
    costs = [MAX_COST] * SIZE
    queue = [] # 우선 순위 큐

    # 그래프 정보 추가
    for src, dst, cost in times:
        graph[src][dst] = cost

    # 시작점 => 큐에 삽입
    heapq.heappush(queue, (0, K)) # cost, start_node
    costs[K] = 0 # 시작 노드 cost => 0 초기화

    # bfs
    while queue:
        cost, cur_node = heapq.heappop(queue)

        # 인접 노드 탐색
        adj_nodes = graph[cur_node]
        for adj_node, adj_cost in enumerate(adj_nodes):
            # 인접 노드 X
            if adj_cost == -1:
                continue
            
            # 인접 노드
            temp_cost = cost + adj_cost
            if temp_cost < costs[adj_node]:
                costs[adj_node] = temp_cost # cost값 갱신
                heapq.heappush(queue, (temp_cost, adj_node)) # 큐에 cost갱신 후 삽입

    costs = costs[1:]
    return -1 if max(costs) == MAX_COST else max(costs)


times = [[1,2,1],[2,1,3]]
N = 2
K = 1
print(networkDelayTime(times, N, K))