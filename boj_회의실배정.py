# 회의실 배정
# https://www.acmicpc.net/problem/1931
START, FINISH = 0, 1

def solution(N, sessions):
    answer = 1 # 가능한 회의 개수

    # 회의 끝나는 순, 회의 시작 순으로 정렬 => 최대한 많은 회의를 하기 위함
    # 제일 빨리 끝나는 회의부터 시작해야지 최대한 많은 회의 가능
    # 끝나는 시간이 동일하다면, 시작 시간이 이른 회의부터 시작해야함
    # ex) [1, 4], [2, 4], [4, 4] > [4, 4], [2, 4], [1, 4]
    sessions.sort(key=lambda x: (x[FINISH], x[START]))

    cur_time = sessions[0][FINISH] # 최초 회의 끝나는 시간
    
    # 남은 회의들과의 비교
    idx = 1
    while idx < N:
        start, end = sessions[idx]
        
        # 현재 회의 끝나는 시간 <= 다음 회의 시작
        # 회의가 가능하다면
        # 다음 회의의 끝나는 시간으로 갱신
        if start >= cur_time:
            answer += 1
            cur_time = end
        
        idx += 1

    return answer

N = int(input())
sessions = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, sessions))
