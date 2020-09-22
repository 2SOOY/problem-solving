# 15. 3Sum
# https://leetcode.com/problems/3sum/

# 투포인터 활용
# idx => 전체 루프 O(N) * 투 포인터 O(N) => O(N^2)
def threeSum(nums):
    answer = []

    # 1. 정렬하기 => 투 포인터 이동을 위함
    nums = sorted(nums)

    # 2. 합이 0이 되는 조합 구하기
    for idx in range(len(nums) - 2):
        if idx > 0 and nums[idx] == nums[idx - 1]: # 이전 숫자와 동일 => 이미 처리된 부분
            continue

        left = idx + 1
        right = len(nums) - 1

        while left < right:
            temp_list = [nums[idx], nums[left], nums[right]]
            sum_value = sum(temp_list)

            # 3-1. 합이 0보다 크다 => 작은 값 필요 => right 이동
            if sum_value > 0:
                right -= 1
            
            # 3-2. 합이 0보다 작다 => 큰 값 필요 => left 이동
            elif sum_value < 0:
                left += 1

            # 3-3. 합이 0 => 정답
            else:
                answer.append(temp_list)
                # left와 right의 다음 위치의 숫자가 현재와 같을 경우 => 미리 이동 => 중복 제거를 위함
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return answer

nums = [0, 0, 0]
print(threeSum(nums))