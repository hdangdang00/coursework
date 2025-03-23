"""
2024310003 황다영
"""
import random

def binary_search(num_list, target, start_index=0, count=1):
    median_index = len(num_list) // 2  # 현재 리스트의 중간 인덱스
    index = start_index + median_index  # 원본 리스트의 인덱스

    # 현재 리스트의 중간 인덱스 값이 목표 값과 같을 때
    if num_list[median_index] == target:
        return index, count
    # 현재 리스트의 중간 인덱스 값이 목표 값보다 작을 때 (목표 값이 더 큰 경우이므로 오른쪽 절반을 탐색한다)
    elif num_list[median_index] < target:
        return binary_search(num_list[median_index + 1 :], target, index + 1, count + 1)
    # 현재 리스트의 중간 인덱스 값이 목표 값보다 클 때 (목표 값이 더 작은 경우이므로 왼쪽 절반을 탐색한다)
    else:
        return binary_search(num_list[:median_index], target, start_index, count + 1)


num_list = sorted(
    random.sample(range(1, 100), 8)
)  # 정수 8개로 이루어진 오름차순 리스트 생성

target = random.choice(num_list)  # 리스트에서 무작위 값 하나를 목표 값으로 설정

index, count = binary_search(num_list, target)

print("정렬된 리스트:", num_list)
print("찾을 값:", target)
print(f"{target} 값은 인덱스 {index}에 있습니다.(탐색 횟수: {count})")
