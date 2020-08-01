# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque


# DFS 이용하기
def dfs(numbers, target, idx, result):
    answer = 0

    # 배열 내 원소 전부 선택
    if idx == len(numbers):
        return 1 if target == result else 0

    # 현재 값 기준 +다음 값, -다음 값
    answer += dfs(numbers, target, idx + 1, result + numbers[idx])
    answer += dfs(numbers, target, idx + 1, result - numbers[idx])

    return answer


def solution1(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)

    return answer


# BFS 이용하기
def solution2(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))  # idx : 몇 번째 원소 선택, result : 누적 계산 값

    while queue:
        idx, result = queue.popleft()

        # 주어진 배열의 원소 전부 선택했을 경우
        if idx == len(numbers):
            if result == target:
                answer += 1
            continue

        # 1개의 pop value에 대해 +, - 값 연산해서 큐에 넣기
        queue.append((idx + 1, result + numbers[idx]))
        queue.append((idx + 1, result - numbers[idx]))

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution1(numbers, target))  # 5
print(solution2(numbers, target))  # 5
