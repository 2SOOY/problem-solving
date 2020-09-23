# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq

def findCheapestPrice(n, flights, src, dst, K):
    queue = []
    graph = defaultdict(list)

    # graph 초기화
    for start, end, cost in flights:
        graph[start].append([end, cost])
    
    heapq.heappush(queue, [0, K, src]) # 최초 노드 큐에 담기 (비용, 경유수, 노드)

    while queue:
        cost, step, cur_node = heapq.heappop(queue) # 항상 최단거리에 대해 탐색을 진행
        
        # 도착지점 => 최단거리
        if cur_node == dst:
            return cost

        # 최대 K개의 노드를 경유할 수 있음
        # K개 이상의 노드를 거쳤을 경우 탐색 종료
        if step >= 0: # ** 범위 설정 주의
            for adj_node, adj_cost in graph[cur_node]:
                temp_cost = adj_cost + cost
                heapq.heappush(queue, [temp_cost, step - 1, adj_node])

    # K개 이상을 경유 or 도착할 수 없음
    return -1


n = 11
edges = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src= 0
dst = 2
k = 4

print(findCheapestPrice(n, edges, src, dst, k))