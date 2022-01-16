from random import randint


def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    rotto = []
    while len(rotto) < n:
        num = randint(1,45)
        if num not in rotto:
            rotto.append(num)
        
    return rotto

def draw_winning_numbers():
    # 코드를 작성하세요.
    arr = generate_numbers(7)
    return sorted(arr[:6])+arr[6:]

def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    count = 0
    for i in numbers:
        if i in winning_numbers:
            count +=1
    
    return count

def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    price = 0
    match = count_matching_numbers(numbers,winning_numbers[:6])
    for i in numbers:
        if i==winning_numbers[6]: 
            bonus = 1
    if match == 6:
        price = 1000000000  
    elif match == 5 and bonus == 1:
        price = 50000000
    elif match == 5:
        price = 1000000
    elif match ==4:
        price = 50000
    elif match == 3:
        price = 5000
        
    return price