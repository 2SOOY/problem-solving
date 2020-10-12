# 해킹
# https://www.acmicpc.net/problem/10282
from collections import defaultdict
import heapq
MAX = float('inf')

# dijkstra
def bfs(graph, start, check):
    queue = []
    heapq.heappush(queue, [0, start])
    check[start] = 0 # 본인 감염 0초

    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        if cur_time > check[cur_node]: # 큐 내에 존재하는 밀려있는 작업들 pass
            continue

        # 인접노드
        for adj in graph[cur_node]:
            adj_node, adj_time = adj
            
            temp_time = adj_time + cur_time
            # 더 빠르게 감염시킬 수 있다면 => check 배열 갱신 및 queue에 담기
            if temp_time < check[adj_node]:
                check[adj_node] = temp_time
                heapq.heappush(queue, (temp_time, adj_node))
            

def solution(N, graph, start):
    check = [MAX] * (N + 1) # 감염되기까지의 시간
    bfs(graph, start, check) # 감염 시키기

    insfected_info = [t for t in check if t != MAX]
    answer = [len(insfected_info), max(insfected_info)]

    return ' '.join(map(str, answer))

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(D):
        end, start, delay = map(int, input().split())
        graph[start].append((end, delay))

    print(solution(N, graph, C))

