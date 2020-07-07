# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    # 변수
    answer = 0
    bucket = []
    R, C = len(board), len(board[0])
    moves = [move - 1 for move in moves]

    # 크레인 동작
    for move in moves:
        for row in range(R):
            if not board[row][move]:
                continue

            # 인형 O
            picked = board[row][move]
            board[row][move] = 0

            # 바구니 처리
            if bucket:
                if bucket[-1] == picked:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(picked)
            else:
                bucket.append(picked)

            break # 빼먹었음

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))