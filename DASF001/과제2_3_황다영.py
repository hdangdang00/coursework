"""
2024310003 황다영
"""
stock_dict = {'커피우유': 6, '돼지바': 5, '삼각김밥': 2, '우유': 1, '제로콜라': 9} # 키는 제품 종류로, 값은 재고 개수로 작성하여 stock_dict 딕셔너리 선언

print('확인 가능한 재고: ', list(stock_dict.items())) # stock_dict의 key-value 쌍 자체를 목록으로 만든 후 list형으로 변경하여 출력
print('확인 가능한 재고 품목: ', list(stock_dict.keys())) # stock_dict로 key에 대한 목록을 만든 후 list형으로 변환하여 출력

product_name = input('재고를 추가할 물건의 이름을 입력하세요: ') # 재고를 추가할 물건의 이름을 입력받아 product_name 변수에 저장
product_count = int(input('재고를 추가할 물건의 수량을 입력하세요: ')) # 재고를 추가할 물건의 수량을 입력 받은 후, 입력 받은 문자를 정수형으로 변환해서 product_count 변수에 저장

stock_dict[product_name] += product_count # 재고를 추가할 물건의 재고 개수를 가져와 기존 재고 개수에 product_count를 더하여 저장

print('추가 후 재고 현황: ', list(stock_dict.items())) # stock_dict의 key-value 쌍 자체를 목록으로 만든 후 list형으로 변경하여 출력