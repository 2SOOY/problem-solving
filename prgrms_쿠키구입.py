# 쿠키 구입
# https://programmers.co.kr/learn/courses/30/lessons/49995
IMPOSSIBLE = 0

def solution(cookies):
    answer = IMPOSSIBLE
    SIZE = len(cookies)

    # 1개의 index를 기준으로
    # 각각의 구간 합 구하기
    for cur in range(SIZE - 1):
        left, sum_left = cur, cookies[cur] # 왼쪽 부분
        right, sum_right = cur + 1, cookies[cur + 1] # 오른쪽 부분

        while True:
            # 1. 정답 후보 => 최대값 갱신
            if sum_left == sum_right:
                answer = max(answer, sum_left)
            
            # 2. left, right 이동하기
            # 2-1. 왼쪽 합이 작거나 같다 => left 이동해서 합 늘리기
            if sum_left <= sum_right and left > 0:
                left -= 1
                sum_left += cookies[left]
            
            # 2-2. 오른쪽 합이 작거나 같다 => right 이동해서 합 늘리기
            elif sum_right <= sum_left and right < SIZE - 1:
                right += 1
                sum_right += cookies[right]
            
            # 2-3. 더 이상 이동이 불가능
            else:
                break

    return answer

cookies = [1, 1, 2, 3]
print(solution(cookies))

