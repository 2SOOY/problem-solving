# 숫자 게임
# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(team_A, team_B):
    answer = 0
    N = len(team_A) 
    team_A.sort()
    team_B.sort()

    a, b = 0, 0 # A, B팀의 인덱스

    for _ in range(N):
        if b == N: # B팀내 더 이상 사용할 숫자 X 
            break
        
        # A팀 숫자가 큼 => B팀의 다음 큰 숫자로 갱신 
        if team_A[a] >= team_B[b]:
            b += 1
            continue
        
        # 승점 챙기기
        answer += 1
        a += 1
        b += 1

    return answer

team_A = [5, 1, 3, 7]
team_B = [2, 2, 6, 8]
print(solution(team_A, team_B))