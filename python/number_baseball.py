from random import randint


def generate_numbers():
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []

    # 코드를 작성하세요.
    while len(numbers)!= 3:
        num = randint(0,9)
        if num in numbers:
            num = randint(0,9)
        else:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    # 지난 과제의 코드를 붙여 넣으세요.
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.

    while len(new_guess) < 3:
        num = int(input('{}번째 숫자를 입력하세요: '.format(len(new_guess)+1)))
        if num in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        elif num >= 0 and num <=9:
            new_guess.append(num)
        else:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
    return new_guess


def get_score(guess, solution):
    # 지난 과제의 코드를 붙여 넣으세요.
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guess[i]==solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1
    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.

player = take_guess()
while player != ANSWER:
    a,b =get_score(ANSWER,player)
    print('{}S {}B'.format(a,b))
    player = take_guess()
    tries += 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
