# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065
import re
from collections import Counter

def solution_1(s):
    result = []

    # 숫자 성분만 남기기
    s = s[2:-2].split('},{') # },{ **

    # 각 튜플의 길이만큼 정렬
    s.sort(key=lambda x: len(x))
    s = [elements.split(',') for elements in s]

    # 작은 길이의 튜플부터 숫자 추가
    for elements in s:
        for number in elements:
            if int(number) not in result:
                result.append(int(number))
                break

    return result

def solution_2(s):
    result = []

    # 모든 숫자 찾아서 개수 담기
    s = Counter(re.findall('\d+', s)) # 정규 표현식 **

    # 개수가 가장 많은 숫자부터 결과에 추가 **
    # 1. 정렬
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)

    # 2. 추가
    for number, _ in s:
        result.append(int(number))

    return result



s = "{{21},{21,1},{21,1,3},{21,1,3,4}}"
print(solution_1(s))
print(solution_2(s))