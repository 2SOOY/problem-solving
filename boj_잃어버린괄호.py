# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

operator = '+-'

# 숫자와 연산자를 분리하기 위한 함수
def translate_expression(expression):
    numbers = []
    operators = []
    temp = ''

    for char in expression:
        if char not in operator:
            temp += char # 숫자의 경우 문자 이어 붙이기
            continue
        
        # 연산자의 경우
        # 지금까지 저장한 숫자 추가, 연산자 추가
        # 숫자 정보 초기화
        numbers.append(int(temp))
        operators.append(char)
        temp = ''
    
    numbers.append(int(temp))

    return [numbers, operators]


# 숫자, 연산자 리스트가 주어졌을 때, 계산하는 함수
def calculate(numbers, operators):
    answer = numbers[0]

    for i in range(len(operators)):
        if operators[i] == '-':
            answer -= numbers[i + 1]
        else:
            answer += numbers[i + 1]

    return answer


# 풀이 1. index를 이용하여 풀기
def solution(expression):
    answer = 0
    numbers, operators = translate_expression(expression)
    
    # 최소값 계산을 위해 만들 새로운 숫자, 연산자 리스트
    new_numbers = [numbers[0]]
    new_operators = []

    for i in range(len(operators)):
        # - 나올 시, 다음 -가 나오기 전까지 => 괄호를 한꺼번에 칠 수도 있음 => 최소값
        # - 연산자 => 새로운 숫자, 연산자 배열에 정보 추가
        if operators[i] == '-':
            new_numbers.append(numbers[i + 1])
            new_operators.append(operators[i])
        
        # + 연산자 => 전부 더한다
        else:
            num1 = new_numbers.pop()
            num2 = numbers[i + 1]
            new_numbers.append(num1 + num2)

    answer = calculate(new_numbers, new_operators)

    return answer


# 풀이2. split 적극 사용
def solution2(expression):
    answer = 0
    # 1. 표현식 '-' 단위로 분리하기
    expression = expression.split('-')

    numbers = []

    # 2. 분리된 작은 표현식 집합에 대해 합 계산하기
    for temp in expression:
        temp = list(map(int, temp.split('+')))
        numbers.append(sum(temp))

    # 3. 최종적으로 남은 숫자들의 -를 진행하면서 값 도출하기
    answer = numbers[0]
    for i in range(1, len(numbers)):
        answer -= numbers[i]

    return answer

expression = input()
print(solution2(expression))