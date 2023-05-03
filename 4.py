import sys
menu = [2000,3000,4000,4000,4500,3000]
print('메뉴를 선택해주세요: 해당 메뉴의 번호를 입력하세요.')
print('1-아메리카노, 2-카페라뗴, 3-카라멜마끼야또, 4-카페모카, 5-딸기라떼, 6-핫초코')
num = int(input('메뉴번호: '))
if num>6 or num<0:
    print('메뉴에 없는 번호입니다.')
    sys.exit()
jan = int(input('몇 잔? '))
total = menu[num-1] * jan
print(f'금액은 {total}원입니다.')