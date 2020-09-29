# 트로피 진열
# https://www.acmicpc.net/problem/1668

def solution(N, trophies):
    left_answer, right_answer = 1, 1
    left, right = 0, len(trophies) - 1
    left_height, right_height = trophies[left], trophies[right]

    # 투 포인터 사용
    while left < right:
        print(left, right)
        # 가장 높은 지점에서 종료됨
        # left -> | <- right
        if left_height < right_height:
            left += 1
            if left_height < trophies[left]:
                left_height = trophies[left]
                left_answer += 1
        else:
            right -= 1
            if right_height < trophies[right]:
                right_height = trophies[right]
                right_answer += 1

    return [left_answer, right_answer]

N = int(input())
trophies = [int(input()) for _ in range(N)]
for answer in solution(N, trophies):
    print(answer)