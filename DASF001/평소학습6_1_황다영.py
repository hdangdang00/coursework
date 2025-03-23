"""
2024310003 황다영
"""
print('두 개의 정수를 입력해주세요.')

num1 = int(input('정수1 입력: ')) # 정수1을 입력받아 int형으로 변경 후 num1 변수에 저장
num2 = int(input('정수2 입력: ')) # 정수2을 입력받아 int형으로 변경 후 num2 변수에 저장

if num1 > num2: # num1이 num2보다 클 경우
    print(f'정수1 빼기 정수2는 {num1 - num2}입니다.') # num1 - num2의 연산 결과를 출력한다.
elif num1 < num2: # num2가 num1보다 클 경우
    print(f'정수2 빼기 정수1는 {num2 - num1}입니다.') # num2 - num1의 연산 결과를 출력한다.
else: # num1과 num2가 같을 경우
    print('정수1은 정수2와 같습니다.')