# 음악프로그램
# https://www.acmicpc.net/problem/2623
from collections import deque, defaultdict

IMPOSSIBLE = 0

# 위상 정렬
def bfs(N, graph, counts, queue):
    result = []
    # cf) 큐에 원소 개수가 2개 이상이라면 => 여러 정렬 순서가 가능함
    while queue:
        cur = queue.popleft()
        result.append(cur)

        # 인접 노드 탐색 => 내 순서 뒤에 오는 노드들
        for adj in graph[cur]:
            counts[adj] -= 1 # 카운트 감소
            
            # 모든 선행 순서에 대한 처리 완료 => 큐에 해당 노드 추가
            if counts[adj] == 0: 
                queue.append(adj) 

    return result

def print_answer(result):
    for node in result:
        print(node)
    return

def solution(N, graph, counts):
    result = []
    queue = deque()

    # count가 0인 노드 큐에 넣기
    for i in range(1, N + 1):
        if counts[i] == 0:
            queue.append(i)
    
    # bfs를 통해 위상정렬 진행
    result = bfs(N, graph, counts, queue)
    
    # result 배열의 길이
    # 만약 result에 모든 node가 들어가지 않았을 경우
    # 순서간에 사이클이 발생했다는 의미 내포
    if len(result) == N:
        print_answer(result)
    else:
        print(IMPOSSIBLE)
    return


N, M = map(int, input().split())
graph = defaultdict(list)
counts = [0] * (N + 1)

for _ in range(M):
    info = list(map(int, input().split()))[1:]
    for i in range(len(info) - 1):
        start = info[i]
        end = info[i + 1]

        graph[start].append(end) # ex) [1, 2], [1, 3] => 1:[2, 3] 
        counts[end] += 1

solution(N, graph, counts)