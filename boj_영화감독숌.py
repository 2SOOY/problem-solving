# 영화감독 숌
# https://www.acmicpc.net/problem/1436

target = '666'

def solution(N):
    count = 0
    number = 665

    while True:
        if target in str(number):
            count += 1
        
        if count == N:
            return number

        number += 1

N = int(input())
print(solution(N))


# cf => 666만 포함여부 확인 by 나머지 연산
def is_possible(number):
    while number:
        remainder = number % 1000 # 10진수의 맨 뒤의 3자리 확인하기 (n % 10^3)
        
        # 뒤 세자리가 666인지 체크
        if remainder == 666: 
            return True

        number /= 10 # 뒤에 한자리씩 날리기

    return False