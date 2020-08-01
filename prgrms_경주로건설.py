# 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

direcion_info = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
ROAD, WALL = 0, 1


# 이전 방향과 현재 진행할 방향을 비교하여 비용 계산
def calc_cost(prev_cost, prev_direction, cur_direction):
    cost = 0
    # 초기 원점
    if prev_direction == 'X':
        return 100

    # 같은 방향
    if prev_direction == cur_direction:
        cost = prev_cost + 100
        return cost

    # 코너
    else:
        cost = prev_cost + 600
        return cost


def bfs(R, C, board, check, queue):
    while queue:

        row, col, cost, prev_dir = queue.popleft()

        for direction, (dr, dc) in direcion_info.items():
            n_row, n_col = row + dr, col + dc
            new_cost = calc_cost(cost, prev_dir, direction)

            if 0 <= n_row < R and 0 <= n_col < C \
                    and board[n_row][n_col] == ROAD \
                    and (check[n_row][n_col] == 0 or check[n_row][n_col] >= new_cost):  # ** 같은 경우도 포함해야함 (3번 케이스)

                check[n_row][n_col] = new_cost
                queue.append((n_row, n_col, new_cost, direction))

    return check[R - 1][C - 1]


def solution(board):
    answer = 0
    R, C = len(board), len(board[0])
    check = [[0] * C for _ in range(R)]  # 해당 지점까지 가는데 드는 비용 행렬

    queue = deque()
    queue.append((0, 0, 0, 'X'))  # 출발점 큐에 삽입
    board[0][0] = 1  # 원점 벽으로 막기

    answer = bfs(R, C, board, check, queue)

    return answer


board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))
