# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

PLUS, MINUS, MULTIPLY, DIVIDE = 0, 1, 2, 3

max_val = -1e9
min_val = 1e9

def solution(N, numbers, operators, i, result):
    global min_val
    global max_val
    print(i, operators, '-->', result)
    # 모든 연산자 사용 완료
    # 최소, 최대값 업데이트
    if i == N - 1:
        print('end', result)
        min_val = min(min_val, result)
        max_val = max(max_val, result)
        return
    
    # 남은 연산자 존재 => 계산하기
    # 모든 연산자 if => 모든 연산자들의 순열들을 확인하기 위함
    # 해당 연산자 사용 후 => 다시 돌려 놓을 것
    if operators[PLUS] > 0:
        print('+')
        operators[PLUS] -= 1
        solution(N, numbers, operators, i + 1, result + numbers[i + 1])
        operators[PLUS] += 1

    if operators[MINUS] > 0:
        print('-')
        operators[MINUS] -= 1
        solution(N, numbers, operators, i + 1, result - numbers[i + 1])
        operators[MINUS] += 1

    if operators[MULTIPLY] > 0:
        print('*')
        operators[MULTIPLY] -= 1
        solution(N, numbers, operators, i + 1, result * numbers[i + 1])
        operators[MULTIPLY] += 1

    if operators[DIVIDE] > 0:
        print('/')
        operators[DIVIDE] -= 1

        if result < 0:
            solution(N, numbers, operators, i + 1, -(abs(result) // numbers[i + 1]))
        else:
            solution(N, numbers, operators, i + 1, result // numbers[i + 1])

        operators[DIVIDE] += 1

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

solution(N, numbers, operators, 0, numbers[0])
print(max_val)
print(min_val)
