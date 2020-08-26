# combination
# nCr 구하기 by 재귀

def dfs(N, list, pick, check, result, cur):
    # pick개 뽑기 완료 => 조합 추가
    if cur == pick:
        temp = ''
        for i in range(N):
            if check[i] == False:
                continue
            temp += list[i]
        
        result.append(temp)
        return
    
    # main 로직
    # 반복문의 시작 시점 **
    # combination은 순서가 없기 때문에
    # 순열과 달리 현재 뽑은 것부터 반복문을 돌려야 한다. range(cur, N)
    for i in range(cur, N):
        if check[i] == False:
            check[i] = True # 뽑고
            dfs(N, list, pick, check, result, cur + 1) # 조합을 구했다면
            check[i] = False # 뽑았던 것 돌려놓고 => 다음 반복문으로 이동
            
    return

# list의 원소 중 pick개 만큼 뽑는 combination을 구하는 함수
def combination(list, pick):
    N = len(list)
    result = [] # combination 결과
    check = [False] * N # 해당 원소 선택 여부를 나타내는 배열

    dfs(N, list, pick, check, result, 0)
    
    return result

list = ['a', 'b', 'c', 'd', 'e']
print(combination(list, 3))