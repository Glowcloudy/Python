# 1부터 n까지 정수의 합 구하기

def sum_1ton(num):
    """1부터 n까지 정수의 합"""
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum

x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')