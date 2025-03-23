"""
2024310003 황다영
"""
def factorial(n): # n을 매개변수로 받아 n!을 구하는 factorial 함수 선언
    result = 1 # 결과값을 저장할 result 함수를 1로 초기화
    for i in range(0, n): # 0부터 n - 1까지 i를 1씩 증가시키며 반복
        result *= (i + 1) # result * (i + 1)을 계산한 값을 result에 저장
    print(result) # result 값 출력

factorial(4) # factorial 함수 호출 하면서 매개변수로 4를 넘김