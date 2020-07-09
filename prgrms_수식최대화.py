# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations


# +,-,* 에 대한 수식 계산
def calcuate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


# 숫자와 연산자 분리하는 함수
def divide_expression(expression):
    start = 0
    numbers = []
    operators = []

    # 연산자에 따라 숫자, 연산자 분리하기
    for idx in range(len(expression)):
        if expression[idx] in '*+-':
            numbers.append(int(expression[start: idx]))
            operators.append(expression[idx])
            start = idx + 1

    # 마지막 숫자 처리
    numbers.append(int(expression[start:]))

    return numbers, operators


def solution(expression):
    answer = 0

    # 연산 우선순위 경우의 수
    operators_cases = permutations('*+-', 3)
    # 숫자, 연산자
    numbers, operators = divide_expression(expression)

    # 각각의 우선순위에 따른 계산
    for case in operators_cases:
        _numbers = numbers.copy()
        _operators = operators.copy()

        # 우선순위에 따른 연산자 순회
        for op in case:
            num_stack = []
            op_stack = []
            num_stack.append(_numbers[0])

            # 남아 있는 연산자 순회
            for idx in range(len(_operators)):
                num_stack.append(_numbers[idx + 1])

                # 해당 우선순위 연산자 처리
                if op == _operators[idx]:
                    num1 = num_stack.pop()
                    num2 = num_stack.pop()
                    num_stack.append(calcuate(num2, num1, op))  # 순서 주의할 것 **

                else:
                    op_stack.append(_operators[idx])

            # 남은 숫자 및 연산자 갱신
            _numbers, _operators = num_stack.copy(), op_stack.copy()

        answer = max(answer, abs(num_stack[0]))

    return answer


expression = "100-200*300-500+20"
print(solution(expression))
