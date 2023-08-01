# 2자리 양수 값 만을 받기

while True:
    n = int(input())
    if n >= 10 and n <= 99:  # 10 <= n <= 99 와 동일 의미를 가지고 있다. 드모르간 법칙을 사용한다면 not(n < 10 or n > 99) 로 표현 가능 하다 
        break
print(n)



