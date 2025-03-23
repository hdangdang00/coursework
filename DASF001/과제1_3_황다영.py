"""
2024310003 황다영
"""
price = int(input('물건값을 입력: ')) # 물건값을 입력 받은 후, 정수형으로 변환하여 price 변수에 저장
bills_count = int(input('1000원 지폐개수: ')) # 1000원 지폐개수를 입력 받은 후, 정수형으로 변환하여 bills_count 변수에 저장
coin_count = int(input('500원 동전개수: ')) # 500원 동전개수를 입력 받은 후, 정수형으로 변환하여 coin_count 변수에 저장

paid_money = (bills_count * 1000) + (coin_count * 500) # 사용자가 지불한 값을 계산((1000원 지폐개수 * 1000) + (500원 동전개수 * 500))하여 paid_money 변수에 저장
change = paid_money - price # 거스름 돈을 계산(사용자가 지불한 값 - 물건값)하여 change 변수에 저장

print('<거스름 돈>',  change, sep = '\n') # change 값을 출력