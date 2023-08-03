# reverse the mutable sequence

from typing import Any, MutableSequence

# a로 mutable sequence를 받아서 가운데 중심으로 양끝 자료들 위치를 바꾼다
def reverse_array(a: MutableSequence) -> None: # 반환 값의 자료형을 지정하지 않는다? 
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    
if __name__ == "__main__":
    nx = int(input("# of elements: "))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f"input x[{i}] value: "))
    
    reverse_array(x)

    print("reversed the sequence")
    for i in range(nx):
        print(f"x[{i}] value : {x[i]}")

# 리스트 x의 원소를 역순으로 정렬해줄 수 있다. 
x.revsere()
y = list(reversed(x)) # x의 원소를 역순으로 정렬하는 이터러블 객체를 생성. list() 함수에 넣어줘야 한다. 
