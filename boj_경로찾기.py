# 경로찾기
# https://www.acmicpc.net/problem/11403

import sys
sys.setrecursionlimit(10 ** 6)


# 방법1 - DFS
def dfs(N, graph, check, start, cur):
    # 인접 노드 DFS
    for adj_node in range(N):
        if graph[cur][adj_node] and check[adj_node] == False:

            # ** 기존 dfs방식과 달리 방문 확인을 반복문 내부에서 진행함 
            # => (0, 0) 같은 경우까지 확인하기 위함
            check[adj_node] = True 
            graph[start][adj_node] = 1 # 해당 방문 지점 graph에 표시
            dfs(N, graph, check, start, adj_node)


# 방법1 - DFS
def solution1(graph):
    N = len(graph)

    for start in range(N):
        for end in range(N):
            
            # start ~ end 이동 가능
            if graph[start][end]:
                continue
            
            # 바로 이동이 불가능한 경우 => DFS
            check = [False] * N # 이동 가능 노드 배열
            dfs(N, graph, check, start, start)

    return


# 방법2 - 플로이드 와샬 
def solution2(graph):
    V = len(graph)
    for mid in range(V): # 거칠 경로
        for start in range(V): # 시작점
            for end in range(V): # 도착점
                # 처음 ~ 중간, 중간 ~ 도착 경로가 존재한다면
                # 처음 ~ 도착 경로 역시 존재함.
                if graph[start][mid] and graph[mid][end]:
                    graph[start][end] = 1 
    
    return 


V = int(input())
graph = [list(map(int, input().split())) for _ in range(V)]
solution1(graph)
# solution2(graph)

for row in graph:
    print(' '.join(map(str, row)))