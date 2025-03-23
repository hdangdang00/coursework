"""
2024310003 황다영
"""
S = '2024년 03월 20일 Wednesday' # S 변수에 문자열 저장

year = S[:4] # 문자열 첫 글자부터 4번째 사이에 있는 모든 글자를 가져와서 year에 저장
month = S[6:8] # 문자열 6번쨰부터 8번쨰 사이에 있는 모든 글자를 가져와서 month에 저장
day = S[10:12] # 문자열 10번쨰부터 12번째 사이에 있는 모든 글자를 가져와서 day에 저장
week = S[14:] # 문자열 14번째부터 마지막 위치에 있는 모든 글자를 가져와서 week에 저장

date = year + month + day + week # year, month, day, week 문자열을 모두 합친 후 date 변수에 저장

print(date) # date 출력