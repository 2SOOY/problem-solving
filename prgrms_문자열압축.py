# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def compress(s, n):
    result = ''
    # n 등분
    sub_strings = [s[i:i+n] for i in range(0, len(s), n)]

    # 압축 진행
    count = 1
    for idx in range(1, len(sub_strings)):
        if sub_strings[idx] == sub_strings[idx - 1]:
            count += 1

        else:
            temp = str(count) if count != 1 else ''
            result += (temp + sub_strings[idx - 1])
            count = 1

    # 마지막 sub string 처리 **
    if count != 1:
        result += (str(count) + sub_strings[-1])
    else:
        result += sub_strings[-1]


    return result

def solution(s):
    answer = len(s)

    # 1글자 ~ 절반까지 압축하기
    for div_num in range(1, (len(s) // 2) + 1): # +1 **
        answer = min(answer, len(compress(s, div_num)))

    return answer

s = "xababcdcdababcdcd"
print(solution(s))