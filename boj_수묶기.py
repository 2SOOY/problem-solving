# 수 묶기
# https://www.acmicpc.net/problem/1744

# 숫자들 묶어서 계산하는 함수
def calculate(nums):
    answer = 0

    while nums:
        if len(nums) >= 2:
            n1, n2 = nums.pop(), nums.pop() # 두 수 추출

            multi = n1 * n2
            plus = n1 + n2 # plus를 구하는 이유 1,1 같은 경우 => 1 + 1 > 1 * 1

            answer += max(multi, plus)

        else:
            answer += nums.pop()

    return answer

def solution(N, numbers):
    answer = 0

    # 1. 양수, 음수, 0 집합 각각 구하기
    plus_nums = [num for num in numbers if num > 0]
    minus_nums = [num for num in numbers if num < 0]
    zeros = [num for num in numbers if num == 0]

    # 2. 정렬하기
    # 양수집합은 오름차순, 음수집합은 내림차순
    if plus_nums:
        plus_nums.sort()
    
    if minus_nums:
        minus_nums.sort(reverse=True)
    
    # 3. 음수 집합의 길이가 홀수 & 0이 존재한다면 => 묶어서 음수 제거 가능
    if zeros and len(minus_nums) % 2:
        minus_nums = minus_nums[1:]

    # 4. 주어진 양수, 음수 집합 계산하기
    answer += calculate(plus_nums)
    answer += calculate(minus_nums)

    return answer

N = int(input())
numbers = [int(input()) for _ in range(N)]
print(solution(N, numbers))