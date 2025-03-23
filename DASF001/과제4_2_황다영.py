"""
2024310003 황다영
"""
def sum(x, y): # x와 y를 매개변수로 받아 x, y의 합을 구하는 sum 함수 선언
    return x + y # x와 y의 합을 return 한다

def mult(x, y): # x와 y를 매개변수로 받아 x, y의 곱을 구하는 mult 함수 선언
    return x * y # x와 y의 곱을 return 한다

n1, n2 = 3, 5 # n1에 3, n2에 5 할당 
print('두 수의 합:', sum(n1, n2)) # sum 함수 호출 하면서 매개변수로 n1과 n2를 넘김, return 값 출력
print('두 수의 곱:', mult(n1, n2)) # mult 함수 호출 하면서 매개변수로 n1과 n2를 넘김, return 값 출력