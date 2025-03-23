"""
2024310003 황다영
"""
avg_credit = float(input('학과의 평균 학점: ')) # 학과의 평균 학점을 입력 받은 후, 입력 받은 문자를 실수형으로 변환해서 avg_credit 변수에 저장

electronics = 3 # electronics 변수에 전자전기학 이수 학점 값 저장
linear_algebra = 3 # linear_algebra 변수에 선형대수 이수 학점 값 저장
computer_graphics = 3 # computer_graphics 변수에 컴퓨터그래픽 이수 학점 값 저장
sw_coding = 2 # sw_coding 변수에 컴퓨팅사고와SW코딩 이수 학점 값 저장

total_credit = electronics + linear_algebra + computer_graphics + sw_coding # 이수 학점의 총합을 구해서 total_credit에 저장

a = ((3.5 * electronics) + (3.0 * linear_algebra) + (4.5 * computer_graphics) + (4.5 * sw_coding)) / total_credit # A 학생의 학점 총합(이수학점 * 성적의 합) / 이수 학점의 총합을 계산하여 A 학생의 평균 학점을 구해 a 변수에 저장
b = ((2.5 * electronics) + (3.5 * linear_algebra) + (4.0 * computer_graphics) + (3.0 * sw_coding)) / total_credit # B 학생의 학점 총합(이수학점 * 성적의 합) / 이수 학점의 총합을 계산하여 B 학생의 평균 학점을 구해 b 변수에 저장
c = ((3.5 * electronics) + (3.0 * linear_algebra) + (3.5 * computer_graphics) + (4.0 * sw_coding)) / total_credit # C 학생의 학점 총합(이수학점 * 성적의 합) / 이수 학점의 총합을 계산하여 C 학생의 평균 학점을 구해 c 변수에 저장

print() # 줄 바꿈
print(f'A 학생의 평균 학점: {a:.3f}') # f-string을 이용해 A 학생의 평균 학점 값을 저장하고 있는 a를 소수점 세번째 자리까지 출력
print() # 줄 바꿈
print(f'B 학생의 평균 학점: {b:.3f}') # f-string을 이용해 B 학생의 평균 학점 값을 저장하고 있는 b를 소수점 세번째 자리까지 출력
print() # 줄 바꿈
print(f'C 학생의 평균 학점: {c:.3f}') # f-string을 이용해 C 학생의 평균 학점 값을 저장하고 있는 c를 소수점 세번째 자리까지 출력
print() # 줄 바꿈
print('학과의 평균 학점보다 높은 학생 여부:', a > avg_credit or b > avg_credit or c > avg_credit) # 학과의 평균 학점보다 높은 학생 여부를 비교 연산자(<, >)와 논리 연산자(or)를 통해 계산하여 출력 