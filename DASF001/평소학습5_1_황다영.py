"""
2024310003 황다영
"""
class_a = {'Kim', 'Lee', 'Park', 'Choi', 'Harry'} # class_a 세트에 A수업 수강자 저장
class_b = {'Choi', 'Jung'} # class_b 세트에 B수업 수강자 저장
class_c = {'Kim', 'Jung', 'Choi'} # class_c 세트에 C수업 수강자 저장

print('1: ', class_a & class_b) # A, B 수업을 모두 수강한 사람은 집합 A와 B의 교집합이다.
print() # 줄바꿈
print('2: ', class_a - (class_b | class_c)) # A 수업만 수강한 사람은 집합 A에서 집합 B와 C의 합집합을 뺀 나머지이다.
print() # 줄바꿈
print('3: ', class_a & class_b & class_c) # A, B, C 수업을 모두 수강한 사람은 집합 A, B, C의 교집합이다.