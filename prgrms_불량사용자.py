# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations


def is_possible_id(banned_id, user_id):
    if len(banned_id) != len(user_id):
        return False

    for idx in range(len(banned_id)):
        if banned_id[idx] == '*':
            continue
        if banned_id[idx] != user_id[idx]:
            return False

    return True


def solution(user_ids, banned_ids):
    # 모든 유저 아이디의 순열 구하기 nPr(n : 유저 수 / r : banned 유저 수)
    candiate_ids = list(map(list, permutations(user_ids, len(banned_ids))))
    result = set()

    # 구한 순열에 대해서 banned_id에 매칭하기
    # 한 유저 아이디 집합에 대해
    for candiate in candiate_ids:
        is_possible = True
        for idx in range(len(banned_ids)):
            # 각각의 아이디의 banned id 가능 체크하기
            if not is_possible_id(banned_ids[idx], candiate[idx]):
                is_possible = False
                break

        if is_possible:
            # 유저 아이디 집합 => 정렬 및 tuple화 => set에 추가하기 위함
            result.add(tuple(sorted(candiate)))

    return len(result)


user_ids = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_ids = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_ids, banned_ids))
