# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

result = []


def dfs(tickets, check, path, node):
    # 모든 티켓 사용 O => 경로 추가
    if all(check):
        result.append(path.copy()) # path : 참조형 변수 => 복사본 필요
        return 

    # 모든 티켓 순회
    for i in range(len(tickets)):
        start, end = tickets[i]

        # 사용하지 않은 티켓에 대해 DFS
        if start == node and check[i] == False:
            check[i] = True
            path.append(end)
            dfs(tickets, check, path, end)
            path.pop()
            check[i] = False


def solution(tickets):
    answer = []
    check = [False] * len(tickets) # 티켓 사용여부 배열
    START ='ICN' # 시작점
    path = [START]

    dfs(tickets, check, path, START)
    answer = sorted(result)[0] # 알파벳 순으로 빠른 곳 => 정답

    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets)) # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']