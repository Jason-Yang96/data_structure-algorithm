# 선형 검색. 원하는 key 값이 여러개라면 가장 먼저 발견한 idx를 반환. 원소의 값이 정렬되지 않은 상태에서 검색할 때 사용하는 유일한 방법 

from typing import Any, Sequence

def seq_search(a: Sequence, key:Any) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i # 만약 sequence a에서 원하는 key 값을 찾게 된다면 그 key 값이 있었던 index를 반환한다.
        i += 1

if __name__ == "__main__":
    num = int(input("원소 수 입력: "))
    x = [None] * num # Sequence의 길이 설정

    for i in range(num):
        x[i] = int(input(f"x[{i}]: ")) # x 리스트에 원소 입력

    ky = int(input("검색할 값 입력: "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 없다.")
    else:
        print(f"검색값은 x[{idx}]에 있다.")