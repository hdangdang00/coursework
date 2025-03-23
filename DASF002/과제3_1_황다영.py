"""
2024310003 황다영
"""
def addNumber(num):
    if num == 1: # num이 1일 때
        return 1 # 1을 return 함
    # num이 1이 아닐 때
    return num + addNumber(num - 1) # num에 addNumber(num - 1)의 return 값을 더하여 return 함

print(addNumber(10)) # addNumber에 매개변수로 10을 넘겨 호출하고 return 값을 출력 함
print(addNumber(15)) # addNumber에 매개변수로 15를 넘겨 호출하고 return 값을 출력 함