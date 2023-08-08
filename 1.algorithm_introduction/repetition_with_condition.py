# n개를 출력, w개 마다 줄을 바꾸기
n = int(input())
w = int(input())

""" for i in range(n):
    print("*", end="")
    if i % w == w - 1:
        print()

if n % w :   # 나머지가 0이 아닌 경우 True로 받아들여지는 것인가? 
    print()
     """

# 조건문을 n번 반복하지 않도록. 더 효율적인 코드를 짜기. 
for _ in range(n//w):
    print("*"*w)

rest = n % w
if rest:
    print("*"*rest)