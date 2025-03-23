"""
2024310003 황다영
"""
score_list = [] # 비어있는 score 리스트 선언

score1 = int(input('평가 점수1: ')) # 평가 점수1을 입력받아 int형으로 변경 후 score1 변수에 저장
score2 = int(input('평가 점수2: ')) # 평가 점수2를 입력받아 int형으로 변경 후 score2 변수에 저장
score3 = int(input('평가 점수3: ')) # 평가 점수3을 입력받아 int형으로 변경 후 score3 변수에 저장

score_list.append(score1) # score1을 score_list 리스트 끝에 추가
score_list.append(score2) # score2를 score_list 리스트 끝에 추가
score_list.append(score3) # score3을 score_list 리스트 끝에 추가

total = sum(score_list) # score_list 리스트 요소의 합을 total 변수에 저장
avg = total / len(score_list) # total / score_list 리스트의 길이로 평균을 구해 avg 변수에 저장

print('심사위원 총 점수:', total) # total 출력
print('심사위원 평균 점수:', avg) # avg 출력