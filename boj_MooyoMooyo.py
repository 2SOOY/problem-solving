# Mooyo Mooyo
# https://www.acmicpc.net/problem/16768

from collections import deque


EMPTY = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 하나의 뿌요에 대해 연결된 뿌요들을 얻는 함수
# BFS 이용
def get_mooyos(board, check, row, col):
    R, C = len(board), len(board[0])
    result = [] # 연결된 뿌요들의 결과를 담을 리스트
    queue = deque() 
    queue.append((row, col))
    result.append((row, col))
    check[row][col] = True

    while queue:
        row, col = queue.popleft()

        for dr, dc in delta:
            n_row, n_col = row + dr, col + dc
            if 0 <= n_row < R and 0 <= n_col < C \
            and board[n_row][n_col] == board[row][col] \
            and check[n_row][n_col] == False:

                queue.append((n_row, n_col))
                result.append((n_row, n_col))
                check[n_row][n_col] = True
    
    return result


# 뿌요들을 터뜨린 후 보드판을 업데이트 하는 함수 
def update_board(board):
    R,C = len(board), len(board[0])

    for col in range(C):
        temp_col = deque() # 공중에 떠 있는 뿌요를 담을 큐
        for row in range(R):

            if board[row][col] == EMPTY:
                continue

            temp_col.append(board[row][col])
        
        # 한 col에 대해서 모든 row 조회가 끝났을 때,
        # 큐에 담겨진 뿌요들을 col의 바닥으로 내리기
        for new_row in range(R - len(temp_col)):
            board[new_row][col] = EMPTY
        for new_row in range(R - len(temp_col), R):
            board[new_row][col] = temp_col.popleft()

    return


def solution(board, K):
    R, C = len(board), len(board[0])
    check = [[False] * C for _ in range(R)]
    
    while True:
        flag = True

        for row in range(R):
            for col in range(C):
                if board[row][col] == EMPTY:
                    continue

                result = get_mooyos(board, check, row, col)
                # 연결된 뿌요들이 K개 이상이면 업데이트 필요
                if len(result) >= K:
                    flag = False
                    for r, c in result:
                        board[r][c] = EMPTY

        # 보드판 업데이트 및 check행렬 초기화
        update_board(board)
        check = [[False] * C for _ in range(R)]

        if flag:
            break
        
    return board


N, K = map(int, input().split())
board = []
for _ in range(N):
    row = list(input())
    if row[-1] == '\r': # WSL 사용 시 => '\r'도 같이 입력받고 있음
        row.pop()
    board.append(row)
board = [list(map(int, row)) for row in board]

result = solution(board, K)
for row in result:
    print(''.join(map(str, row)))


"""
input
6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223

output
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
"""