# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def get_binary(num):
    result = []
    
    while num:
        remainder = num % 2
        num //= 2

        result.append(remainder)
    
    return result[::-1]


def count_one(binary):
    return binary.count(1)


def solution(n):
    target = count_one(get_binary(n))

    while True:
        n += 1
        temp = count_one(get_binary(n))

        if temp == target:
            return n

n = 78
print(solution(n))