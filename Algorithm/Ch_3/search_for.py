# for문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any)->int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i    # 검색 성공
    return -1   # 검색 실패 

if __name__ == "__main__":
    num = int(input('원소 개수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))    # 검색할 key를 입력받음

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')