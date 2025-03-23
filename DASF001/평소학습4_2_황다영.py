"""
2024310003 황다영
"""
num_tuple = tuple(range(10, 0, -2)) # range 사용하여 (10, 8, 6, 4, 2) 튜플을 선언하여 num_tuple에 저장

print('range를 활용해 선언한 튜플:', num_tuple) # num_tuple 출력

num_tuple = list(num_tuple) # num_tuple 튜플을 리스트로 변경 후 num_tuple에 저장
num_tuple.append('컴퓨팅 사고') # '컴퓨팅 사고'를 num_tuple 리스트 끝에 추가

num_tuple = tuple(num_tuple) # num_tuple 리스트를 튜플로 변경 후 num_tuple에 저장

print('문자열 추가 후 튜플:', num_tuple) # num_tuple 출력