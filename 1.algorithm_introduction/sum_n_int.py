# 판단 반복 구조 ==> structure of deciding whether to repeat

def sum_n(n):
    result = 0
    i = 1 # control the repetition, 카운터용 변수라고 불린다. 
    while i <= n:
        result += i
        i += 1
    return result


# 양수만을 받을 수 있도록 만든다

while True: # 의도적으로 무한 루프를 만들어 놓은 상태
    n = int(input())
    if n > 0:
        break # 특정 조건을 만족시키면 무한 루프를 탈출할 수 있음

print(sum_n(n))

