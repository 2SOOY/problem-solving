# 알파벳
# https://www.acmicpc.net/problem/1987

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(R, C, board, queue):
    answer = 0
    while queue:
        row, col, path = queue.pop()
        answer = max(answer, len(path))

        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc

            if 0 <= n_row < R and 0 <= n_col < C \
            and board[n_row][n_col] not in path:
                queue.add((n_row, n_col, path + board[n_row][n_col]))

    return answer


def solution(R, C, board):
    answer = 0
    queue = set()
    queue.add((0, 0, board[0][0]))

    answer = bfs(R, C, board, queue)
    return answer

R, C = map(int, input().split())
board = []
for _ in range(R):
    row = list(input().rstrip())
    board.append(row)

print(solution(R, C, board))