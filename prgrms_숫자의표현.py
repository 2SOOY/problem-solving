# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(target):
    answer = 0

    # 연속된 숫자의 시작값
    for start in range(1, target + 1):
        temp = 0

        # 연속한 숫자들 더해보기
        while temp <= target:
            if temp == target:
                answer += 1
                break

            temp += start
            start += 1

    return answer

n = 15
print(solution(n))
