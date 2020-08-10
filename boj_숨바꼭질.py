# 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque

MAX_LEN = 100001 # 최대 이동 범위

def bfs(K, check, queue):
    while queue:
        loc, step = queue.popleft()

        if loc == K:
            return step

        # 1초에 -1, +1, *2 만큼 이동 가능
        for next_loc in [loc - 1, loc + 1, 2 * loc]:
            if 0 <= next_loc < MAX_LEN \
            and check[next_loc] == False:

                queue.append((next_loc, step + 1))
                check[next_loc] = True # 이미 방문한 곳은 재방문하지 않도록
        

def solution(N, K):
    queue = deque()
    check = [False] * MAX_LEN

    queue.append((N, 0)) # 최초 위치, 0초 시작
    check[N] = True

    return bfs(K, check, queue)

N, K = map(int, input().split())
print(solution(N, K))