# 시퀀스 원소의 최댓값 출력
# 동적 언어는 변수의 타입을 일일이 명시하지 않아도 되지만, 잘못된 타입을 사용해 오류를 범하는 경우가 생긴다. 이에 따라 타입을 명시하는 수요가 늘어나고 있다.
# 혹시 더 알아보고 싶으면 do it 자료구조/알고리즘 입문 파이썬 편 79p 확인
# 함수 어노테이션과 if __name__ == "__main__"은 대체 뭐냐?

from typing import Any, Sequence

def max_of(a: Sequence) -> Any: # Any는 제약이 없는 임의의 자료형을 반환한다는 의미. Sequence는 시퀀스형을 의미함. 시퀀스 자료형이라면 리스트든, 튜플이든, 문자열이든 상관없음
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

# __name__은 모듈 이름을 나타내는 변수 
# 스크립트 프로그램이 직접 실행될 때 모듈 이름은 "__main__"
# 직접 실행되지 않고 임포트 될 때는 원래의 모듈 이름
# 이 max.py 파일이 직접 실행 될 때만 아래 if 문이 실행된다. 
# 만약에 max.py가 다른 파일에서 import 될 때는 if 문이 실행되지 않는다. 
# 스크립트의 재사용 가능성이 높아지는 것이다. 

if __name__ == '__main__':
    print("print max")
    print(__name__)
    num = int(input("# of array: "))
    x = [None] * num    
    for i in range(num):
        x[i] = int(input(f"input x[{i}] value: "))
    
    print(f"max: {max_of(x)}")

# 근데 그냥 append 써도 되는거 아니냐? 굳이 입력할 원소 개수만큼 자리 마련해 둬야 할 필요가 있나? 효율성에 차이가 있는걸까? 더 알고 싶다. 
""" if __name__ == '__main__':
    print("print max")
    num = int(input("# of array: "))
    x = []     
    for i in range(num):
        n = int(input(f"input x[{i}] value: "))
        x.append(n)

    print(f"max: {max_of(x)}")
 """