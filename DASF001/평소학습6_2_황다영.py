"""
2024310003 황다영
"""
num = int(input('어디까지 계산할까요: ')) # 어디까지 계산할 지를 입력받아 int형으로 변경 후 num 변수에 저장
result = 1 # 1부터 num까지의 정수의 곱을 저장할 변수이기 때문에 1로 초기화 해줌

for i in range(0, num): # 0 부터 num - 1까지 i값을 1씩 증가하며 반복
    result *= (i + 1) # result 값에 i + 1 값을 곱한 값을 result에 저장

print(f'1부터 {num} 까지의 정수의 곱: {result}') # 1부터 num까지의 정수의 곱인 result 값을 출력