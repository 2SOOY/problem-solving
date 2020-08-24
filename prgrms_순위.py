# 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

WIN, LOSE = 1, -1


# 그래프 생성 함수
# 이긴 것과 진 것에 대해 data를 구분하여 그래프 생성
def generate_graph(n, results):
    graph = [[0] * n for _ in range(n)]

    for winner, loser in results:
        winner, loser = winner - 1, loser - 1

        graph[winner][loser] = WIN
        graph[loser][winner] = LOSE

    return graph


# 본인의 순위를 알 수 있는 사람 수 구하기
def find_possible_grade(graph):
    answer = 0

    for row in graph:
        # n명의 player중 n-1개의 승부 결과가 존재하는지 파악
        # 본인을 제외한 타인과의 승부 결과를 전부 알 수 있다면,
        # 본인의 순위를 알 수 있음
        if row.count(0) == 1:
            answer += 1

    return answer


# 방법 1 - 플로이드 와샬
def update_graph(n, graph):
    # win, lose score update
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                # win score에 대한 업데이트
                if graph[start][mid] == WIN and graph[mid][end] == WIN:
                    graph[start][end] = WIN

                # lose score에 대한 업데이트
                if graph[start][mid] == LOSE and graph[mid][end] == LOSE:
                    graph[start][end] = LOSE
    return


def solution1(n, results):
    answer = 0
    graph = generate_graph(n, results)
    update_graph(n, graph)
    answer = find_possible_grade(graph)

    return answer


# 방법 2 - DFS
def dfs(n, graph, check, start, node, flag):
    check[node] = True

    for idx in range(n):
        if graph[node][idx] == flag and check[idx] == False:

            graph[start][idx] = flag
            dfs(n, graph, check, start, idx, flag)

    return


# 방법 2 - DFS
def solution2(n, results):
    answer = 0
    graph = generate_graph(n, results)

    for cur in range(n):
        check_win = [False] * n
        check_win[cur] = True
        check_lose = [False] * n
        check_lose[cur] = True

        for adj in range(n):

            # cur이 adj를 이길 수 있다면
            # adj가 이길 수 있는 모든 사람을 이길 수 있음
            # adj에 대해서 DFS
            if graph[cur][adj] == WIN:
                flag = WIN
                dfs(n, graph, check_win, cur, adj, flag)
            
            # 반대로 cur이 adj한테 진다면
            # adj가 지는 사람들 모두에게 cur은 짐
            if graph[cur][adj] == LOSE:
                flag = LOSE
                dfs(n,graph, check_lose, cur, adj, flag)

    answer = find_possible_grade(graph)

    return answer

n = 7
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [2, 6], [2, 7], [6, 5], [5, 7]]
print(solution1(n, results))
print(solution2(n, results))