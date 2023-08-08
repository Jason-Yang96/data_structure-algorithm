# 선형 검색 + 보초법

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key:Any) -> int:
    a = copy.deepcopy(seq) #seq 깊은 복사, a 리스트에 원소가 추가되더라도 seq에는 영향이 없다. 
    a.append(key) #key 마지막에 추가

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i #key 값을 찾아서 break 했지만 그 i가 원래 seq의 길이라면 검색에 실패한 것이다. 그래서 -1을 반환한다.  

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