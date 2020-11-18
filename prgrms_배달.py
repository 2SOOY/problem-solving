# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978
# 전형적인 다익스트라 문제

from collections import defaultdict
import heapq

MAX = float('inf')

def make_graph(road):
    graph = defaultdict(list)
    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    return graph

def dijkstra(graph, costs):
    initial_city = 1
    queue = [(0, initial_city)]
    costs[initial_city] = 0

    while queue:
        cost, cur = heapq.heappop(queue)
        # 이전에 힙에 추가됐지만 우선순위에 밀려 사용되지 않는 것 패스
        if cost > costs[cur]:
            continue
        
        # 인접 도시 탐색
        for adj_city, adj_cost in graph[cur]:
            temp_cost = adj_cost + costs[cur] # 현재 도시 ~ 인접 도시 까지 비용
            
            # 시작점 ~ 인접 마을 비용 vs 시작점 ~ 현재 마을 ~ 인접 마을 비용 
            if temp_cost < costs[adj_city]:
                costs[adj_city] = temp_cost
                heapq.heappush(queue, (temp_cost, adj_city))

    return

def solution(N, road, K):
    answer = 0
    graph = make_graph(road)
    costs = [MAX] * (N + 1) # 1번 마을 ~ M 마을 까지 최소 비용 담은 리스트
    dijkstra(graph, costs) # 1번 마을 ~ 각각의 마을까지 최소 비용 갱신
    answer = len([cost for cost in costs if cost <= K])

    return answer

N = 5 
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K =  3
print(solution(N, road, K))