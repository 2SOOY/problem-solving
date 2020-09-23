# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    # solve without division & O(N)
    answer = [1] * len(nums)

    # 1. 자신의 왼쪽 성분들 곱한 값
    left_prod = 1
    for i in range(len(nums)):
        answer[i] = left_prod
        left_prod *= nums[i] # 이전 요소에서 곱한 결과 값을 캐싱하여 사용함

    # 2. 자신의 오른쪽 성분들 곱한 값
    # 대신, 공간복잡도를 O(N)으로 유지하기 위해 answer배열 그대로 사용
    right_prod = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] *= right_prod
        right_prod *= nums[i] 

    return answer
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))