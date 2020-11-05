# 최소값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(arr1,arr2):
    answer = 0
    arr1.sort()
    arr2.sort(reverse=True)

    temp = [arr1[i] * arr2[i] for i in range(len(arr1))]
    answer = sum(temp)

    return answer

arr1 = [1, 4, 2]
arr2 = [5, 4, 4]
print(solution(arr1, arr2))