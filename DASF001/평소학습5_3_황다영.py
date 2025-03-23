"""
2024310003 황다영
"""
python = 3 # python 변수에 파이썬 이수 학점 값 저장
linear_algebra = 3 # linear_algebra 변수에 선형대수 이수 학점 값 저장
computer_graphic = 3 # computer_graphic 변수에 컴퓨터그래픽 이수 학점 값 저장
sw_coding = 2 # sw_coding 변수에 컴퓨팅사고와SW코딩 이수 학점 값 저장

total = (python * 3.5) + (linear_algebra * 3.0) + (computer_graphic * 4.5) + (sw_coding * 4.5) # total 변수에 (이수학점 * 성적)을 모두 더한 값인 총 학점 값을 저장한다. 
avg = total / (python + linear_algebra + computer_graphic + sw_coding) # avg 변수에 총 학점 / 이수학점 총합 값을 저장한다.

print('이수학점 총합:', python + linear_algebra + computer_graphic + sw_coding) # python, linear_algebra, computer_graphic, sw_coding를 모두 더한 값을 출력한다.
print() # 줄바꿈
print(f'평균 학점: {avg:.2f}') # f-string을 이용해 평균 학점 값을 저장하고 있는 avg를 소수점 두번째 자리까지 출력한다.