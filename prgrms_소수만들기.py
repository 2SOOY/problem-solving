# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


# 방법1. 소수 판단 함수
def is_prime(number):
    for i in range(2, int(number ** (0.5)) + 1):
        if number % i == 0:
            return False

    return True


# 방법1. 소수 판단 함수 이용
def solution1(nums):
    answer = 0
    sum_candidates = combinations(nums, 3)
    sum_candidates = [sum(candidate) for candidate in sum_candidates]

    for candidate in sum_candidates:
        if is_prime(candidate):
            answer += 1

    return answer


# 방법2. 에라토스테네스의 체
def get_prime(number):
    checked = [0] * (number + 1)

    for idx in range(2, number):
        if checked[idx] == 1:
            continue

        for next_idx in range(2 * idx, number + 1, idx):
            checked[next_idx] = 1

    primes = [idx for idx, num in enumerate(checked) if num == 0 and idx > 1]

    return set(primes)


# 방법2. 에라토스테네스의 체 이용
def solution2(nums):
    answer = 0
    sum_candidates = combinations(nums, 3)
    sum_candidates = [sum(candidate) for candidate in sum_candidates]

    primes = get_prime(max(sum_candidates))

    for sum_number in sum_candidates:
        if sum_number in primes:
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))
