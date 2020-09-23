# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    profit = 0
    low = 1e6

    # 큰 이익을 얻기 위해선 저점에서 사고 고점에서 팔아야함
    # 가격이 변할 때마다 저점을 갱신 => 저점 기준 차이 값을 구함
    for i in range(len(prices)):
        low = min(low, prices[i])
        profit = max(profit, prices[i] - low)
    
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))