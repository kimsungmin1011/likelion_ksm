import random
x=random.randint(50,100)
y=random.randint(50,100)
z=random.randint(50,100)
print(f'랜덤 정수: {x},{y},{z}')
if x>=y>=z:
    first=x
    second=y
    third=z
elif x>=z>=y:
    first=x
    second=z
    third=y
elif y>=x>=z:
    first=y
    second=x
    third=z
elif y>=z>=x:
    first=y
    second=z
    third=x
elif z>=x>=y:
    first=z
    second=x
    third=y
elif z>=y>=x:
    first=z
    second=y
    third=x

print(first,second,third)
if x==y or x==z or y==z:
    print('같은 수 있음')