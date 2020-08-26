# permutation
# nPr 구하기 by 재귀

def dfs(N, list, pick, check, cur, result):
    # pick개 뽑기 완료 => 순열 추가
    if cur == pick:
        temp = ''
        for i in range(N):
            if check[i] == False:
                continue
            temp += list[i]
        
        result.append(temp)
        return
    
    # 재귀 
    for i in range(N):
        # 뽑지 않은 것에 대해
        if check[i] == False: 
            check[i] = True # 뽑고
            dfs(N, list, pick, check, cur + 1, result) # 재귀 돌리기
            check[i] = False # 재귀 결과 순열 결과 저장 시 => 뽑았던 것 돌려놓기

    return

# 주어진 list에서 pick만큼 순열 구하기
def permutation(list, pick):
    N = len(list)
    check = [False] * len(list) # 현재 뽑힌 원소들을 나타낼 리스트
    result = [] # 순열 결과

    dfs(N, list, pick, check, 0, result) # 아무것도 뽑지 않음 => 0 부터 재귀

    return result

list = ['a', 'b', 'c', 'd', 'e']
print(permutation(list, 3))