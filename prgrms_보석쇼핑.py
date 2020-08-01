# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


# left ~ right까지 보석 담기
def solution1(gems):
    answer = [1, len(gems)]
    target = len(set(gems))

    left, right = 0, 0
    picked_gems = defaultdict(int)
    picked_gems[gems[right]] += 1

    while True:
        # 보석이 부족한 경우 => right 이동 => 보석 추가
        if len(picked_gems) < target:
            right += 1
            # 모든 보석 조회 완료
            if right == len(gems):
                break
            picked_gems[gems[right]] += 1
            continue

        # 모든 보석이 존재할 경우 => answer값 갱신 => left 이동 => 보석 제거
        if len(picked_gems) == target:
            # 더 적게 선택했다면 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]

            # 같을 경우 갱신 X => 숫자 작은 순부터 출력해야 하기 때문 => 이미 앞에서 처리 완료
            # 보석 제거
            picked_gems[gems[left]] -= 1
            if picked_gems[gems[left]] == 0:
                del picked_gems[gems[left]]

            left += 1

    return answer


# left ~ right - 1 까지 보석 담기.
# 2번 풀이의 경우 아래와 같은 논리 순서로 진행해야함
# 모든 보석이 존재함 => right 순회 완료 => 보석 부족함
def solution2(gems):
    answer = [1, len(gems)]
    target = len(set(gems))

    picked_gems = defaultdict(int)

    left, right = 0, 0

    while True:
        # 모든 보석 존재
        if len(picked_gems) == target:
            if right - left < answer[1] - answer[0] + 1:
                answer = [left + 1, right]

            picked_gems[gems[left]] -= 1
            if picked_gems[gems[left]] == 0:
                del picked_gems[gems[left]]

            left += 1
            continue

        if right == len(gems):
            break

        # 모든 보석 존재 X
        if len(picked_gems) < target:
            picked_gems[gems[right]] += 1
            right += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "DIA", "SAPPHIRE"]
print(solution1(gems))  # [3, 8]
print(solution2(gems))  # [3, 8]
