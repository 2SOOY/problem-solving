# 게임 맵 최단거리
# https://school.programmers.co.kr/courses/10098/lessons/59589


from collections import deque

LOAD, WALL = 1, 0

# BFS - 1 : 큐에 이동 거리 정보 넣기
def bfs1(R, C, board, check, queue):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        row, col, step = queue.popleft()

        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if 0 <= n_row < R and 0 <= n_col < C \
            and board[n_row][n_col] == LOAD \
            and check[n_row][n_col] == False:

                if (n_row, n_col) == (R-1, C-1):
                    return step + 1

                queue.append((n_row, n_col, step + 1)) # 큐 내부에 이동거리 담기
                check[n_row][n_col] = True
    
    return -1


def solution1(board):
    R, C = len(board), len(board[0])
    answer = 0
    check = [[False] * C for _ in range(R)]

    queue = deque([(0, 0, 1)])
    check[0][0] = True

    answer = bfs1(R, C, board, check, queue)

    return answer


# BFS - 2 : 현재 큐에 담긴 개수만큼 반복문 시행 => 이동거리 1번 카운팅
def bfs2(R, C, board, check, queue):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    step = 1

    while queue:

        step += 1
        for _ in range(len(queue)): # 큐에 담긴 인접 노드만큼 반복
            row, col = queue.popleft()

            for dr, dc in delta:
                n_row, n_col = row + dr, col + dc

                if 0 <= n_row < R and 0 <= n_col < C \
                and board[n_row][n_col] == LOAD \
                and check[n_row][n_col] == False:

                    if (n_row, n_col) == (R - 1, C - 1):
                        return step

                    queue.append((n_row, n_col))
                    check[n_row][n_col] = True

    return -1


def solution2(board):
    R, C = len(board), len(board[0])
    answer = 0
    check = [[False] * C for _ in range(R)]

    queue = deque([(0, 0)])
    check[0][0] = True

    answer = bfs(R, C, board, check, queue)

    return answer





board = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(board))
