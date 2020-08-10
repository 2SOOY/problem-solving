# 숨바꼭질4
# https://www.acmicpc.net/problem/13913

from collections import deque

MAX_LEN = 100001 # 최대 이동 범위

def bfs(N, K, check, queue, path):
    while queue:
        loc, step = queue.popleft()

        if loc == K:

            # 경로 추적하기
            result = []
            while loc != N:         # 시작 위치가 나올때까지 탐색
                result.append(loc)  # 현재 위치 추가
                loc = path[loc]     # 이전 위치로 변경
            result.append(N) # 마지막 최초 위치 추가

            return step, result[::-1]

        # 1초에 -1, +1, *2 만큼 이동 가능
        for next_loc in [loc - 1, loc + 1, 2 * loc]:
            if 0 <= next_loc < MAX_LEN \
            and check[next_loc] == 0:

                queue.append((next_loc, step + 1))
                check[next_loc] = step + 1 # 이미 방문한 곳은 재방문하지 않도록
                path[next_loc] = loc       # 다음 위치 기준 이전 위치 갱신


def solution(N, K):
    queue = deque()
    check = [0] * MAX_LEN # 해당 위치 방문 여부 정보를 담는 배열
    path = [0] * MAX_LEN  # index기준 이전 위치의 정보를 담는 배열 ** 

    queue.append((N, 0)) # 최초 위치, 0초 시작
    check[N] = 0

    return bfs(N, K, check, queue, path)

N, K = map(int, input().split())
step, path = solution(N, K)

print(step)
print(' '.join(map(str, path)))