# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

def is_possible(stones, k, mid):
    zeros = 0

    for stone in stones:

        # m번째 사람이 해당 돌을 밟을 수 없다
        if stone - mid < 0: # ** <= 이면 밟을 수 있는 경우도 포함하는 것 
            zeros += 1

            # 밟을 수 없는 돌이 k개 => 건널 수 없음
            if zeros == k:
                return False

        # 밟을 수 있는 돌이 생기면 초기화
        else:
            zeros = 0

    return True 


def solution(stones, k):
    answer = 1
    start = 1 # k와 stone의 값은 1 이상의 값을 갖음
    end = max(stones)

    # binary search
    while start <= end:
        mid = (start + end) // 2

        # mid 명의 사람이 돌다리를 건널 수 있는지 판별
        if is_possible(stones, k, mid):
            answer = mid # 정답 갱신
            start = mid + 1
        else:
            end = mid - 1

    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))