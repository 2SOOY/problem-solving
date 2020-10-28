# 후위 표기식
# https://www.acmicpc.net/problem/1918

ALPHA = [chr(65 + i) for i in range(26)] # A - Z
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

def solution(expression):
    result = ''
    stack = [] # 연산자를 담을 stack

    for char in expression:
        # 1. 문자 => 바로 추가
        if char in ALPHA:
            result += char
        
        # 2. 연산자 => 우선 순위에 따라 계산하기
        else:
            # 2-1. 사칙 연산
            if char in '+-*/':
                # 자신보다 우선순위가 높은 연산자들 POP후 결과식에 추가하기
                while stack and priority[stack[-1]] >= priority[char]:
                    result += stack.pop()
                
                stack.append(char)
            
            # 2-2-1. 열린 괄호
            elif char == '(':
                stack.append(char)
            
            # 2-2-2. 닫힌 괄호
            else:
                while stack:
                    cur = stack.pop()

                    if cur == '(':
                        break

                    else:
                        result += cur
                        continue
    
    # 남은 연산자들 처리
    while stack:
        result += stack.pop()

    return result

expression = input()
print(solution(expression))