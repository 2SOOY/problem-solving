# Subset
# 주어진 집합의 모든 부분 집합 구하기

def dfs(N, list, check, result, level):
    # Subset 추가하기
    # depth가 list의 길이와 같아진다 => 모든 리스트에 대한 선택 완료
    if level == N:
        temp = ''
        for i in range(N):
            if check[i] == False:
                continue
            temp += list[i]

        result.append(temp)
        return
    
    # 재귀 돌리기
    # level => depth이자 list의 인덱스를 나타냄
    check[level] = True # 해당 원소 선택 O
    dfs(N, list, check, result, level + 1)
    check[level] = False # 해당 원소 선택 X
    dfs(N, list, check, result, level + 1)
    return

def subset(list):
    N = len(list)
    result = []
    check = [False] * len(list)

    dfs(N, list, check, result, 0)

    return result

list = ['a', 'b', 'c']
print(subset(list))