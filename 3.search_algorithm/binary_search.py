from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0 # 검색 범위 시작 인덱스
    pr = len(a) - 1 # 검색 범위 마지막 인덱스

    while True:
        pc = (pl+pr)//2 # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc # 검색 성공
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:   # 이건 어떤 상황일까? 무슨 상황이긴 그냥 검색 실패지
            break 
    return -1

if __name__ == "__main__":
    num = int(input("원소 수 입력: "))
    x = [None] * num
    
    x[0] = int(input("x[0]: "))

    for i in range(1,num):
        while True:
            x[i] = int(input(f"x[{i}]: "))
            if x[i] >= x[i-1]:
                break

    ky = int(input("찾고자 하는 값 입력: "))

    idx = bin_search(x, ky)

    if idx == -1:
        print("찾는 값이 없음")

    else:
        print(f"찾는 값은 x[{idx}]에 있다.")
