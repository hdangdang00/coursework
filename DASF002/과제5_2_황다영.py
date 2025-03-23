"""
2024310003 황다영
"""
def generate_subsets(nums):
    subsets = [[]]  # subsets에 공집합을 추가

    for num in nums:
        length = len(subsets)  # 현재 subsets의 길이를 구해 length에 저장
        for i in range(0, length):
            subset = subsets[i].copy()  # subsets[i]를 복사하여 subset에 저장(원본이 변경되지 않도록 하기 위함)
            new_subset = subset + [num]  # subset과 num을 합쳐 새로운 부분 집합을 생성함
            subsets.append(new_subset)  # subsets에 새로운 부분 집합인 new_subset 추가함

    return subsets


nums = [1, 2, 3]
subsets = generate_subsets(nums)
for subset in subsets:
    print(subset)
