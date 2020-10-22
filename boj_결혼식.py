# 결혼식
# https://www.acmicpc.net/problem/5567
from collections import defaultdict, deque

SG = 1

# 상근이와의 관계 구하기 bfs
def bfs(V, graph):
    queue = deque()
    check = [0] * (V + 1)

    queue.append((SG, 0))
    check[SG] = 1

    while queue:
        cur, diff = queue.popleft()

        for friend in graph[cur]:
            if check[friend]:
                continue

            queue.append((friend, diff + 1))
            check[friend] = diff + 1

    return check         

def solution(V, graph):
    check = bfs(V, graph)
    temp = [num for num in check if 0 < num < 3]

    return len(temp) - 1 # 본인 제외

V = int(input())
E = int(input())
graph = defaultdict(list)

for _ in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

print(solution(V, graph))