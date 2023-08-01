# sum of numbers from a to b or b to a
def sum_a_to_b(a,b):
    if a > b :
        a , b  =  b , a # 값 교환을 위한 단일 대입문
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum

a = int(input())
b = int(input())

print(f"sum of from a to b: {sum_a_to_b(a,b)}")