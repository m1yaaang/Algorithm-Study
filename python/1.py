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
    match = count_matching_numbers(numbers,winning_numbers)
    if match == 6:
        price = 1000000000
    elif match == 5 and count_matching_numbers(numbers,winning_numbers[6])==1:
        price = 50000000
    elif match == 5:
        price = 1000000
    elif match ==4:
        price = 50000
    elif match == 3:
        price = 5000
        
    return price

# 테스트
print(count_matching_numbers([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(count_matching_numbers([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))