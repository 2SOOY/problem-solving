# 문서 검색
# https://www.acmicpc.net/problem/1543

REPLACEMENT = '*'
def solution(document, taret):
    answer = 0
    # 1.target 문자 => 치환하기
    document = document.replace(target, REPLACEMENT)

    # 2. target 문자 개수 세기
    for ch in document:
        if ch == REPLACEMENT:
            answer += 1

    return answer

document = input()
target = input()
print(solution(document, target))