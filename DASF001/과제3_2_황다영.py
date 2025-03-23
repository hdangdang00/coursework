"""
2024310003 황다영
"""
star_cnt = int(input('끝 층의 별 개수: ')) # 끝 층의 별 개수를 입력받아 int형으로 변경 후 star_cnt 변수에 저장

for i in range(1, star_cnt * 2): # 1부터 star_cnt * 2 - 1까지 i값을 1씩 더하며 반복
    if i <= star_cnt: # i가 star_cnt보다 작거나 같을 때
        print('*' * (star_cnt - i + 1)) # star_cnt - i + 1만큼 *을 출력한다.
    else: # i가 star_cnt보다 클 때
        print('*' * (i - star_cnt  + 1)) # i - star_cnt + 1만큼 *을 출력한다.