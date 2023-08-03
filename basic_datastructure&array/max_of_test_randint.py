# max 에서 max_of라는 함수를 불러오기 위해서는 같은 경로에 위치해야 한다. 
# 오우~! max.py 파일의 max_of 함수 재사용 완료!!
import random
from max import max_of

print("check the max # of random number")
num = int(input("input # of random number: "))
lo = int(input("start of random range: "))
hi = int(input("end of random range: "))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f"{x}")
print(f"max number is : {max_of(x)}")