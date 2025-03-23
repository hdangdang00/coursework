"""
2024310003 황다영
"""
num1 = int(input('정수 입력: ')) # 정수를 입력받아 int형으로 변경 후 num1 변수에 저장
num2 = int(input('정수 입력: ')) # 정수를 입력받아 int형으로 변경 후 num2 변수에 저장
sum = 0 # 합을 저장할 sum 변수는 0으로 초기화

if num1 > num2: # num1이 num2보다 클 때
    for i in range(num2, num1 + 1): # num2부터 num1까지 i값을 1씩 더하며 반복
        sum += i # sum 변수에 sum + i 값을 저장
    print(f'{num2}에서 {num1}까지 더하면 {sum}') # num2에서 num1까지 더한 값인 sum 값 출력
else: # num1이 num2보다 크지 않을 때
    for i in range(num1, num2 + 1): # num1부터 num2까지 i값을 1씩 더하며 반복
        sum += i # sum 변수에 sum + i 값을 저장
    print(f'{num1}에서 {num2}까지 더하면 {sum}') # num1에서 num2까지 더한 값인 sum 값 출력