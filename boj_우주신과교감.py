# 우주신과 교감
# https://www.acmicpc.net/problem/1774
import math, heapq
from collections import defaultdict

DIST = 2

def calculate_distance(info, src, dst):
    sx, sy = info[src]
    dx, dy = info[dst]

    x = abs(sx - dx)
    y = abs(sy - dy)

    result = math.sqrt(x ** 2 + y ** 2)
    return result


# union-find의 find 연산
def find_root(parents, node):
    if parents[node] != node:
        parents[node] = find_root(parents, parents[node]) # path compression
    
    return parents[node]

# union-find의 union 연산
def union_root(parents, a, b):
    root_a = find_root(parents, a)
    root_b = find_root(parents, b)

    if root_a == root_b:
        return
    
    # 작은 번호의 노드를 root로 합치기
    if root_a < root_b:
        parents[root_b] = root_a
    else:
        parents[root_a] = root_b



def solution(N, info, connections):
    connections.sort(key=lambda x: x[DIST]) # 거리(비용) 순서대로 정렬
    parents = [i for i in range(N + 1)]
    answer = []

    # MST => 크루스칼
    for edge in connections:
        a, b, distance = edge
        
        if find_root(parents, a) == find_root(parents, b):
            continue

        # root가 다를 경우 union 연산을 통해 노드 연결
        union_root(parents, a, b)
        answer.append(distance)
    
    return sum(answer)


# MAIN
N, E = map(int, input().split())
info = defaultdict(tuple)
connections = []
for i in range(N):
    # 좌표 정보
    x, y = map(int, input().split())
    info[i + 1] = (x, y)

# 모든 노드들 사이의 연결 비용 구하기
for i in range(1, N):
    for j in range(i + 1, N + 1):
        edge = (i, j, calculate_distance(info, i, j))
        connections.append(edge)

for _ in range(E):
    # 연결 정보
    a, b = map(int, input().split())
    edge = (a, b, 0) # 이미 연결이 된 노드 => 비용 0
    connections.append(edge)
    
print(format(solution(N, info, connections), ".2f"))