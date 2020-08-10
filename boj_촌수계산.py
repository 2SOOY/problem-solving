# 촌수계산
# https://www.acmicpc.net/problem/2644

from collections import deque

def bfs(N, matrix, checked, queue, target):
    while queue:
        cur, step = queue.popleft()

        connected_nodes = matrix[cur] # 나와 연결된 노드들
        for idx, connection in enumerate(connected_nodes):
            if connection and checked[idx] == False:
                
                if idx == target:
                    return step + 1

                checked[idx] = True
                queue.append((idx, step + 1)) # 인접 노드 방문 => 촌수 + 1
                
    return -1


def solution(N, matrix, p1, p2):
    answer = 0
    checked = [False] * (N + 1)

    queue = deque()
    queue.append((p1, 0)) # 출발노드, 현재촌수
    checked[p1] = True

    answer = bfs(N, matrix, checked, queue, p2)

    return answer

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())

matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    parent, child = map(int, input().split())
    # 단순히 촌수만 계산하는 문제 : 양방향 그래프로 설계 가능
    matrix[parent][child] = 1
    matrix[child][parent] = 1 

print(solution(N, matrix, p1, p2))
