# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
# 문제 잘 읽기 => 2개 붙어 있는 짝 **

from collections import deque


# queue 사용
def solution1(s):
    stack = []
    string = deque(s)

    while string:
        alpha = string.popleft()
        if stack and stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)

    return 1 if len(stack) == 0 else 0


# loop만
def solution2(s):
    stack = []

    for alpha in s:
        if stack and stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)

    return not stack


s = 'baabaa'
print(solution(s))
