# 암호 만들기
# https://www.acmicpc.net/problem/1759
# 단순 조합 구하기
vowel = 'aeiou'

def solution(N, alphabets):
    answer = []
    alphabets.sort() # 암호는 알파벳순으로 정렬
    check = [False] * len(alphabets) # 알파벳 선택 배열

    def dfs(count, start, result):
        if count == N:
            v_count = 0
            c_count = 0

            # 모음, 자음 개수 카운트
            for alpha in result:
                if alpha in vowel:
                    v_count += 1
                else:
                    c_count += 1
            
            # 조건 만족시 => 비밀번호 가능
            if v_count >= 1 and c_count >= 2:
                answer.append(result)

            return

        # 조합 logic 
        for i in range(start, len(alphabets)):
            if check[i]:
                continue
            
            check[i] = True
            dfs(count + 1, i + 1, result + alphabets[i])
            check[i] = False
    
    dfs(0, 0, '')
    return answer

# MAIN
N, C = map(int, input().split())
alphabets = list(input().split())
answer = solution(N, alphabets)
for password in answer:
    print(password)