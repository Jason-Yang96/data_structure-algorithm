# +, - 를 번갈아 가면서 출력하고 싶은 상태. 근데 굳이 조건문을 n번 돌릴 필요가 있을까? 
n = int(input())

""" for i in range(1, n+1):
    if i % 2:
        print("+", end = "")
    else:
        print("-", end="")
 """

# 개선 

for _ in range(n//2):
    print("+-", end="")

if n % 2: # n이 홀수라면 값이 1로 true가 됨
    print("+", end="")

