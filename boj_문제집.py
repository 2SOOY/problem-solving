# 문제집
# https://www.acmicpc.net/problem/1766

from collections import defaultdict
import heapq

def solution(N, graph, check):
    answer = []
    heap = []

    # 2. 문제 처리
    # 선행 문제가 없는 문제들 => 힙 담기
    for node in range(1, N + 1):
        if check[node]:
            continue
        heapq.heappush(heap, node)
    
    while heap:
        node = heapq.heappop(heap) # 조건3. 낮은 번호의 문제부터 해결하기
        answer.append(node)

        # 뒤이어 풀어야할 문제에 대해 탐색 진행
        for next_node in graph[node]:
            check[next_node] -= 1

            # 더 이상 풀어야할 문제가 없을 경우
            # 힙에 추가
            if check[next_node] == 0:
                heapq.heappush(heap, next_node)

    return answer

N, M = map(int, input().split())
graph = defaultdict(list)
check = [0] * (N + 1)

# 1. graph 생성
# X -> Y => X: 선행 작업 Y: 후행 작업
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    check[end] += 1 # 선행되는 문제수 만큼 count 증가

result = solution(N, graph, check)
print(' '.join(map(str, result)))