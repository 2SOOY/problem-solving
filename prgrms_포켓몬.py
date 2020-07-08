# 포켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter
from itertools import combinations


# Counter 적용 => 포켓몬 종류 별로 분류
def solution(pocketmons):
    answer = 0

    pocketmons_info = Counter(pocketmons)
    pocketmons_info = [[pocketmon, count]
                       for pocketmon, count in pocketmons_info.items()]

    for _ in pocketmons_info:
        answer += 1
        if answer == len(pocketmons) // 2:
            return answer

    return answer


# Set 적용 => 포켓몬 종류 수
def solution_2(pocketmons):
    pocketmon_types = len(set(pocketmons))
    if pocketmon_types >= len(pocketmons) // 2:
        return len(pocketmons) // 2
    else:
        return pocketmon_types


# Combination 적용
# 시간초과
def solution_3(pocketmons):
    answer = 0

    picked_candidates = combinations(pocketmons, len(pocketmons) // 2)
    for candidate in picked_candidates:
        picked = len(set(candidate))
        answer = max(answer, picked)

    return answer


pocketmons = [3, 3, 3, 2, 2, 2]
print(solution(pocketmons))
