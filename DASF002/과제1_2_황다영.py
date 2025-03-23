"""
2024310003 황다영
"""
def findStuNum(name): # 학번을 찾는 함수인 findStuNum 선언
    for stuNum, stuName in stuInfo.items(): # stuInfo 딕셔너리에서 stuNum(학번)과 stuName(이름)을 순차적으로 가져옴
        if stuName == name: # stuName과 name이 같을 때
            return stuNum # 해당 stuNum(학번) 반환

stuInfo = {'2023123456':'정해선', '2022999888':'성균관', '2023777666':'명륜이', '2021666555':'율전이', '2020444222':'응용이'}
stuClassInfo = {'2023123456':[95,58,89], '2022999888':[77,86,94], '2023777666':[85,91,52], '2021666555':[78,85,93], '2020444222':[62,75,97]}

name = input('찾고자 하는 학생의 이름: ') # 찾고자 하는 학생의 이름을 입력 받아 name에 저장

if name in stuInfo.values(): # 입력한 학생이 stuInfo 딕셔너리 value 중에 있을 때
    stuNum = findStuNum(name) # 입력한 학생의 학번을 stuNum에 저장
    stuScoreList = stuClassInfo[stuNum] # stuClassInfo에서 해당 학번의 성적 리스트를 가져옴
    stuScoreAvg = sum(stuScoreList) / len(stuScoreList) # 성적 리스트의 평균을 계산하여 stuScoreAvg에 저장
    print(name, '학생은 성균관대학교 재학생입니다.')
    print(f"{name} 학생의 성적 평균은 {stuScoreAvg:.2f}입니다.") # 입력한 학생의 성적 평균을 소수점 둘째 자리까지 출력
else: # 입력한 학생이 stuInfo 딕셔너리 value 중에 없을 때
    print(name, '학생은 성균관대학교 학생이 아닙니다.')