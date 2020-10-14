# 근우의 다이어리 꾸미기
# https://www.acmicpc.net/problem/16676

def solution(N):
    # 숫자가 중복된만큼 스티커팩이 필요함
    answer = len(N)
    compare = '1' * len(N)

    # 1자리 숫자 => 1팩 가능
    if answer == 1:
        return answer

    # 11111.... 스티커팩이 필요한 최대치
    if int(compare) <= int(N):
        return answer
    else:
        return answer - 1

N = input()
print(solution(N))