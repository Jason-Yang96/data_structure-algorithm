# 약수를 나열하는 프로그램

area = int(input())
for i in range(1, area+1):
    if i*i > area:
        break
    if area % i: continue # 나누어 떨어지지 않는 겨우 다음 명령문을 실행하지 않고 다음 반복문을 실행한다.
    print(f"{area} = {i} x {area//i}")