# Euclid algorithm for gcd

def gcd(x:int, y: int)->int:
    if y== 0:
        return x
    else:
        return gcd(y, x%y)
    
if __name__ == '__main__':
    print('두 정수값의 최대 공약수를 구하시오')

    x = int(input('첫 번째 정수값을 입력하시오.: '))
    y = int(input('두 번째 정수값을 입력하시오.: '))

    print(f'두 정숫값의 최대 공약수는{gcd(x, y)}입니다.')