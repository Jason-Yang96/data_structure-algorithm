# 판단 반복 구조 ==> structure of deciding whether to repeat

def sum_n(n):
    result = 0
    i = 1 # control the repetition, 카운터용 변수라고 불린다. 
    while i <= n:
        result += i
        i += 1
    return result

a = int(input())
print(f'sum of from 1 to n : {sum_n(a)}') 
