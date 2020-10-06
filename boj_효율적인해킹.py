# 효율적인 해킹
# https://www.acmicpc.net/problem/1325
# PyPy 통과 / python3 시간초과

from collections import defaultdict, deque

def bfs(N, graph, counts, node):
    queue = deque()
    check = [False] * (N + 1)

    queue.append(node)
    check[node] = True
    count = 1

    while queue:
        cur = queue.popleft()

        # 해킹 가능한 연결된 컴퓨터
        for adj in graph[cur]:
            if check[adj] == False:
                check[adj] = True
                count += 1 # 개수 추가하기
                queue.append(adj)
    
    return count

def solution(N, graph):
    answer = []
    counts = [0] * (N + 1)
    
    # 모든 컴퓨터에 대해서 한 번씩 해킹해보기
    for node in range(1, N + 1):
        counts[node] = bfs(N, graph, counts, node)

    max_value = max(counts)
    for node in range(1, N + 1):
        if counts[node] == max_value:
            answer.append(node)

    return answer

# main
N, M = map(int, input().split())
graph = defaultdict(list)
# 그래프 생성 주의 => N x N 만큼의 공간을 할당할 때 메모리 초과 발생 
for _ in range(M):
    end, start = map(int, input().split())
    graph[start].append(end)
    
print(' '.join(map(str, solution(N, graph))))