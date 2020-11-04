# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        duration = 0
        for j in range(i + 1, len(prices)):
            duration += 1
            if prices[i] <= prices[j]:
                continue
            
            break       
        
        answer[i] = duration
        
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))