# 성 지키기
# https://www.acmicpc.net/problem/1236

EMPTY, PERSON = '.', 'X'
def solution(R, C, board):
    rows = [0] * R
    cols = [0] * C

    for row in range(R):
        for col in range(C):
            if board[row][col] == PERSON:
                rows[row] += 1
                cols[col] += 1
    
    # row, col 중 빈 곳이 더 많은 쪽에 맞추어 배치하면 된다.
    # 전부 비었을 경우 생각해볼 것
    return max(rows.count(0), cols.count(0))

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

print(solution(R, C, board))

