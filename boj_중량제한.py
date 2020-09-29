# 중량제한
# https://www.acmicpc.net/problem/1939
from collections import defaultdict, deque

# 3. 해당 하중 가능 여부 판단 
def is_possible(N, graph, src, dst, mid):
    queue = deque()
    queue.append(src)
    check = [False] * (N + 1)
    check[src] = True

    while queue:
        cur = queue.popleft()

        for adj, limit in graph[cur]:
            if check[adj]:
                continue

            if limit >= mid: # 주어진 무게에서 견딜 수 있다.
                queue.append(adj)
                check[adj] = True

    # 도착 지점을 방문 했는가 => 방문 했다면 mid라는 무게에서 건널 수 있음
    return check[dst]

def solution(N, graph, src, dst, start, end):
    answer = 0
    # 이분 탐색
    # 무게를 지정 => bfs를 통해 방문이 가능한지 파악

    # 2. 하중에 따른 이분탐색 진행
    while start <= end:
        mid = (start + end) // 2
        if is_possible(N, graph, src, dst, mid):
            answer = mid
            start = mid + 1
            continue

        end = mid - 1

    return answer

N, M = map(int, input().split())
graph = defaultdict(list)
start, end = 1e9, 1
for _ in range(M):
    a, b, limit = map(int, input().split())
    graph[a].append([b, limit])
    graph[b].append([a, limit])

    # 1. 이분 탐색을 위한 start와 end값 지정
    start = min(start, limit)
    end = max(end, limit)

src, dst = map(int, input().split())
print(solution(N, graph, src, dst, start, end))