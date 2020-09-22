# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# 시간 초과 O(N^2)
# 2차원 행렬로 만들어 1row씩 물채우기
EMPTY = 0
WALL = 1

def get_empty_num(row):
    result = 0

    walls = [idx for idx, num in enumerate(row) if num == WALL]
    for idx in range(1, len(walls)):
        result += walls[idx] - walls[idx - 1] - 1

    return result

def trap1(heights):
    result = 0
    R = max(heights)
    C = len(heights)
    board = [[EMPTY] * C for _ in range(R)]

    for idx, height in enumerate(heights):
        for row in range(height):
            board[R - row - 1][idx] = WALL
    
    for row in board:
        result += get_empty_num(row)

    return result


# 방법2 - 투 포인터 활용
# 가장 높은 벽을 기준으로 왼쪽 포인터와 오른쪽 포인터를 옮긴다.
# 가장 높은 벽 기준 나의 높이의 차가 물이 채워질 공간이다.
def trap(heights):
    answer = 0
    start, end = 0, len(heights) - 1
    max_start, max_end = heights[start], heights[end]

    # 둘이 만나기 전까지 반복
    # 결국은 가장 높은 벽에서 만나게 되어 있음
    while start < end:
        # 벽의 최대 높이 갱신
        max_start = max(max_start, heights[start])
        max_end = max(max_end, heights[end])
        
        # 오른쪽의 벽이 더 높은 벽일 경우
        # 왼쪽의 포인트 이동 => 가장 높은 벽에 다가가기 위해
        if max_start <= max_end:
            answer += max_start - heights[start] # 왼쪽 무리 중에 가장 높은 벽의 높이 - 현재 위치
            start += 1 # 왼쪽 포인터 이동
        else:
            answer += max_end - heights[end]
            end -= 1

    return answer


heights = [0,3,0,2,0,1,3,3,2,0,2,1]
print(trap(heights))