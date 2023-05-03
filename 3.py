print("주민번호 7자리를 입력하세요: 예)010428-3")
a = input("주민번호: ")
if (a[0] + a[1]>'23'):
    year = '19'+a[0]+a[1]+'년'
else:
    year = '20'+a[0]+a[1]+'년'

if a[2]=='0':
    month = a[3]+'월'
else:
    month = a[2]+a[3]+'월'

if a[4] == '0':
    day=a[5]+'일생'
else:
    day=a[4]+a[5]+'일생'

if a[7] == '1' or a[7] == '3':
    gender = '남'
elif a[7] == '2' or a[7] =='4':
    gender = '여'
else:
    gender = '성별오류'
print(f'{year} {month} {day}, 성별:{gender}')
