# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    end = len(citations) + 1

    for num in range(end):
        more = len([citation for citation in citations if citation >= num])
        less = len([citation for citation in citations if citation <= num])

        if more >= num and less <= num:
            answer = max(answer, num)

    return answer

citations = [2, 2, 2, 2, 2]
print(solution(citations))