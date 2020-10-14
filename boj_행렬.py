# 행렬
# https://www.acmicpc.net/problem/1080

def toggle(row, col, matrix):
    for r in range(3):
        for c in range(3):
            # XOR : 반전
            # 1 ^ 1 => 0 
            # 0 ^ 1 => 1
            matrix[row + r][col + c] ^= 1 


def is_same(R, C, src, dst):
    for row in range(R):
        for col in range(C):
            if src[row][col] != dst[row][col]:
                return False
    return True


def solution(R, C, src, dst):
    answer = 0

    # (0, 0)을 기준으로 해당 점이 다를 경우 => flip 하기
    # 같게 만들기 위해서는 다른 성분을 무조건 뒤집어야 함 
    for row in range(R - 2):
        for col in range(C - 2):
            # 다른 위치 존재 => 반전
            if src[row][col] == dst[row][col]:
                continue
            
            toggle(row, col, src)
            answer += 1

    return answer if is_same(R, C, src, dst) else -1

R, C = map(int, input().split())
src = [list(map(int, list(input()))) for _ in range(R)]
dst = [list(map(int, list(input()))) for _ in range(R)]

print(solution(R, C, src, dst))
