"""
2024310003 황다영
"""
usage = int(input('전기 사용량 입력 (kwh) >> ')) # 전기 사용량을 입력 받은 후 int형으로 변환해서 usage에 저장

if usage <= 200: # 전기 사용량이 200 이하일 때
    unit_price = 99.3
    basic_price = 910
elif usage >= 201 and usage <= 400: # 전기 사용량이 201 이상이고 400 이하일 때
    unit_price = 187.9
    basic_price = 1600
else: # 전기 사용량이 400 초과일 때
    unit_price = 280.6
    basic_price = 7300

electrocity_charge = int(unit_price * usage + basic_price) # 전기 요금 계산 후 계산 결과를 int형으로 변환하여 electrocity_charge에 저장

print('단가: ', unit_price, '원,', sep="", end=" ") # 단가 출력
print('기본요금: ', basic_price, '원,', sep="", end=" ") # 기본요금 출력
print('전기요금: ', format(electrocity_charge, ','), '원', sep="") # electrocity_charge를 천단위 마다 ,를 추가하여 출력