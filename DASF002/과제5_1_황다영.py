"""
2024310003 황다영
"""
def two_sum_brute_force(nums, target):
    pairs = []  # 합이 target이 되는 두 숫자의 인덱스를 저장할 리스트 pairs
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:  # nums[i]와 nums[j]의 합이 target과 같으면
                pairs.append((i, j))  # pairs에 인덱스인 i와 j를 (i, j) 형태로 추가함
    return pairs


nums = [2, 4, 5, 6, 9, 7, 11, 15, 16, 18]
target = 20
pairs = two_sum_brute_force(nums, target)
print(pairs)
