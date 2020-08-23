# 문명
# https://www.acmicpc.net/problem/14868
from collections import deque

EMPTY = 0
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# find 연산
def find_root(roots, city):
    if roots[city] == city:
        return city
    
    roots[city] = find_root(roots, roots[city])

    return roots[city]

# union 연산
def union_root(N, board, roots, queue):
    global K # 현재 문명 개수

    # 큐에 있는 지역들 탐색
    for row, col in queue:
        cur = board[row][col]
        
        # 인접 지역들 => union 연산
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            # 이미 문명이 퍼진 지역에 대해
            if 0 <= n_row < N and 0 <= n_col < N \
            and board[n_row][n_col] != EMPTY:
                near = board[n_row][n_col]

                # 해당 지역의 root 찾기
                cur_root = find_root(roots, cur)
                near_root = find_root(roots, near)

                # 같은 문명
                if cur_root == near_root:
                    continue
                
                # 다른 문명 => 문명 합쳐주기
                K -= 1 # 문명이 합쳐지면 총 문명 개수 1개 줄이기
                if cur_root < near_root:
                    roots[near_root] = cur_root
                else:
                    roots[cur_root] = near_root

    return


# 문명 퍼뜨리기
def bfs(N, board, queue):
    # 1 depth씩 탐색하기 위해 queue의 길이만큼 bfs
    for _ in range(len(queue)):
        row, col = queue.popleft()

        # 인접 지역 탐색
        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            # 빈 지역에 대해 => 문명 퍼뜨리기
            if 0 <= n_row < N and 0 <= n_col < N \
            and board[n_row][n_col] == EMPTY:

                board[n_row][n_col] = board[row][col]
                queue.append((n_row, n_col))
    return


def solution(N, board, roots, queue):
    global K
    step = 0

    while queue:
        # 문명 합치는 과정을 먼저 하는 이유
        # 처음 주어진 문명들이 전부 이어지 있는 경우도 있음
        union_root(N, board, roots, queue) 

        # 문명을 합친 결과 남은 문명의 개수가 1개
        # 모든 문명 결합 완료
        if K == 1:
            break
        
        # 문명 퍼뜨리기
        bfs(N, board, queue)
        step += 1
    
    return step


# INPUT
N, K = map(int, input().split())
board = [[EMPTY] * N for _ in range(N)]
roots = [city for city in range(K + 1)]
queue = deque()

for idx in range(K):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    row, col = N - 1 - y, x 

    board[row][col] = idx + 1
    queue.append((row, col))

print(solution(N, board, roots, queue))
