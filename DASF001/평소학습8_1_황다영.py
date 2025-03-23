"""
2024310003 황다영
"""
import datetime # datetime 모듈 import

print('첫 날을 입력하세요.')
year = int(input('연도: ')) # 연도 입력 받은 후 int형으로 변환
month = int(input('월: ')) # 월 입력 받은 후 int형으로 변환
day = int(input('일: ')) # 일 입력 받은 후 int형으로 변환

print('**************')

today = datetime.datetime.today() # 현재 날짜와 시간을 가져와서 today 변수에 저장
input_day = datetime.datetime(year, month, day) # 입력 받은 연, 월, 일로 datetime 객체 생성 후 input_day에 저장

difference_day = (today - input_day).days # 오늘 날짜와 입력 날짜 사이의 차이를 구해 difference_day에 저장
d_day = input_day + datetime.timedelta(days=100) - datetime.timedelta(days=1) # 입력한 날짜의 100일 기념일을 계산하여 d_day에 저장

print(f'{difference_day}일 지났고 100일 기념일은 {d_day.year}.{d_day.month}.{d_day.day}입니다.') # difference_day 출력, d_day를 YYYY.M.D형식으로 출력