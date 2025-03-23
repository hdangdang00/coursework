"""
2024310003 황다영
"""
import random # random 모듈 import

def get_rank(matching_num_cnt): # 숫자가 일치하는 개수를 매개변수로 받아 순위를 반환하는 함수
    if matching_num_cnt < 3: # 일치하는 숫자의 개수가 3개 미만일 때 -> 미당첨
        return '미당첨'
    elif matching_num_cnt == 3: # 일치하는 숫자의 개수가 3개일 때 -> 4등
        return '4등'
    elif matching_num_cnt == 4: # 일치하는 숫자의 개수가 4개일 때 -> 3등
        return '3등'
    elif matching_num_cnt == 5: # 일치하는 숫자의 개수가 5개일 때 -> 2등
        return '2등'
    else: # 일치하는 숫자의 개수가 6개일 때 -> 1등
        return '1등'

user_input = input('1이상 20이하의 6개의 숫자를 입력해주세요 ( 예시 :1 2 3)\n입력: ') # 1부터 20사이의 숫자 6개를 입력받아 user_input에 저장

user_num_list = list(map(lambda num : int(num), user_input.split())) # user_input을 띄어쓰기로 구분해 각각의 숫자를 int형으로 변환 후 list형으로 저장
com_num_list = random.sample(range(1, 21), 6) # 1부터 20사이의 6개의 난수를 생성하여 com_num_list에 저장

matching_num_list = list(set(user_num_list) & set(com_num_list)) # 사용자가 입력한 숫자 리스트와 컴퓨터가 입력한 숫자 리스트의 교집합(일치하는 숫자)을 구해 list형으로 변환

print('사용자:', user_num_list) # 사용자가 입력한 숫자 출력
print('컴퓨터:', com_num_list) # 컴퓨터가 입력한 숫자 출력
print(f"일치하는 번호는 {matching_num_list}로, {len(matching_num_list)} 개이며, {get_rank(len(matching_num_list))}입니다.") # 일차하는 번호, 일치하는 숫자의 개수, 일치하는 숫자의 개수에 따른 등수 출력