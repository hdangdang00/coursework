"""
2024310003 황다영
"""
num = int(input('양의 정수 입력: ')) # 양의 정수를 입력받아 int형으로 변경 후 num 변수에 저장
i = 0 # i를 0으로 초기화
while i < num: # i가 num보다 작을 때까지 반복
    print('*' * (i + 1)) # *을 i + 1개 출력
    i += 1 # i 값을 1 증가시킴