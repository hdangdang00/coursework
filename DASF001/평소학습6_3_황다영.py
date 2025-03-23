"""
2024310003 황다영
"""
floor = int(input('층수: ')) # 층수를 입력받아 int형으로 변경 후 floor 변수에 저장

for i in range(0, floor): # 0 부터 floor - 1까지 i값을 1씩 증가하며 반복
    for j in range(floor - i, 0, -1): # floor - i 부터 1까지 j값을 1씩 감소하며 반복
        print('*', end="") # * 출력 (줄바꿈 하지 않음)
    print() # 줄바꿈