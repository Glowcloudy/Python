# 상위 폴더는 같고 다른 폴더에 있는 파일 import 하는 법
import sys
sys.path.append(r'C:\Users\User\python programming\Python\pyhon\Algorithm\Ch_4')

# 불러 올려고하는 .py file
from stack import Stack

def recur(n:int)->int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n -=1
            continue
        if not s.is_empty():
            n =s.pop()
            print(n)
            n = n-2
            continue
        break

x = int(input('정숫값을 입력하세요.: '))

recur(x)