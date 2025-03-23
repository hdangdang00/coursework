"""
2024310003 황다영
"""
lang = int(input('언어 : ')) # 언어 데이터를 입력받아 int형으로 변경 후 lang 변수에 저장
foreign_lang = int(input('외국어 : ')) # 외국어 데이터를 입력받아 int형으로 변경 후 foreign_lang 변수에 저장
science = int(input('과탐 : ')) # 과탐 데이터를 입력받아 int형으로 변경 후 science 변수에 저장

score_dict = {'언어': lang, '외국어': foreign_lang, '과탐': science} # score_dict 딕셔너리에 언어, 외국어, 과탐 key로 lang, foreign_lang, science 데이터 저장

total = sum(list(score_dict.values())) # score_dict 딕셔너리의 value를 모두 가져와서 리스트로 변환 후 리스트 요소의 합을 total 변수에 저장
avg = total / len(score_dict) # total / score_dict 딕셔너리의 길이로 평균을 구해 avg 변수에 저장

print('---------------')

print(list(score_dict.items())) # score_dict 딕셔너리의 key-value 쌍 자체를 목록으로 만든 후 리스트로 변환하여 출력

print('평균:', avg) # avg 출력