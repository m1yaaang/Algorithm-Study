import random

# 코드를 작성하세요.
a = random.randint(1,20)
chance = 4
while chance>0:
    num = int(input("기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "))
    if num == a:
        print('축하합니다. {}번만에 숫자를 맞히셨습니다.'.format(chance))
        break;
    elif num > a:
        print('Down')
        chance -= 1
    else:
        print('Up')
        chance -= 1
if chance <= 0:        
    print('아쉽습니다. 정답은 {}입니다.'.format(a))
